from odoo import _, fields, models,api
from odoo.exceptions import UserError
from odoo.tools import float_compare
import logging
_logger = logging.getLogger(__name__)

class WithholdingTax(models.Model):
     _name = "withholding.tax"
     _inherit = "withholding.tax"
    
class AccountInvoiceWithholdingTax(models.Model):
    
    _name = "account.invoice.withholding.tax"
    _inherit = "account.invoice.withholding.tax"
    
    
class AccountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"

    @api.depends("amount_sp")
    def calcTotalSplit(self):
        for record in self:
            record.split_payment=-1*record.amount_sp
            
    @api.depends("amount_untaxed")
    def calcTotal(self):
        for record in self:
            record.total_with_sp=record.amount_untaxed+record.amount_sp
        
        
    split_payment=fields.Monetary(string="Split Payment", store=True, readonly=True, compute=calcTotalSplit)
    total_with_sp=fields.Monetary(string="Totale Split Payment", store=True, readonly=True, compute=calcTotal)
      
    def set_receivable_line_ids(self):
        """Recompute all account move lines by _recompute_dynamic_lines()
        and set correct receivable lines
        """
        
        self._recompute_dynamic_lines()
        line_client_ids = self.line_ids.filtered(
            lambda l: l.account_id.id
            == self.partner_id.property_account_receivable_id.id
        )
        if self.move_type == "out_invoice":
            for line_client in line_client_ids:
                inv_total = self.amount_sp + self.amount_total
                if inv_total:
                    receivable_line_amount = (
                        self.amount_total * line_client.debit
                    ) / inv_total
                else:
                    receivable_line_amount = 0
                line_client.with_context(check_move_validity=False).update(
                    {
                        "price_unit": -receivable_line_amount,
                        "debit": receivable_line_amount,
                        "amount_currency": receivable_line_amount,
                        "price_total": receivable_line_amount,
                    }
                )

        elif self.move_type == "out_refund":
            for line_client in line_client_ids:
                inv_total = self.amount_sp + self.amount_total
                if inv_total:
                    receivable_line_amount = (
                        self.amount_total * line_client.credit
                    ) / inv_total
                else:
                    receivable_line_amount = 0
                line_client.with_context(check_move_validity=False).update(
                    {
                        "price_unit": -receivable_line_amount,
                        "credit": receivable_line_amount,
                        "amount_currency": receivable_line_amount,
                        "price_total": receivable_line_amount,
                    }
                )
    def _compute_split_payments(self):
        write_off_line_vals = self._build_debit_line()
        line_sp = self.line_ids.filtered(
            lambda l: l.is_split_payment or l.name == _("Split Payment Write Off")
        )
        if line_sp:
            if self.move_type == "out_invoice" and float_compare(
                line_sp[0].debit,
                write_off_line_vals["debit"],
                precision_rounding=self.currency_id.rounding,
            ):
                line_sp[0].with_context(check_move_validity=False).update({"debit": 0})
                self.set_receivable_line_ids()
                line_sp[0].debit = write_off_line_vals["debit"]
            elif self.move_type == "out_refund" and float_compare(
                line_sp[0].credit,
                write_off_line_vals["credit"],
                precision_rounding=self.currency_id.rounding,
            ):
                line_sp[0].with_context(check_move_validity=False).update({"credit": 0})
                self.set_receivable_line_ids()
                line_sp[0].credit = write_off_line_vals["credit"]
        else:
            self.set_receivable_line_ids()
            if self.amount_sp:
                self.line_ids = [(0, 0, write_off_line_vals)]

                       
                
                
class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    @api.depends("amount_tax")
    def calcTotalSplit(self):
        if(self.partner_id.property_account_position_id.name == "Split Payment"):
            for record in self:
                record.split_payment=-1*record.amount_tax
            
    @api.depends("amount_untaxed")
    def calcTotal(self):
        if(self.partner_id.property_account_position_id.name == "Split Payment"):
            for record in self:
                record.total_with_sp=record.amount_untaxed+record.amount_tax
        
        
    split_payment=fields.Monetary(string="Split Payment", store=True, readonly=True, compute=calcTotalSplit)
    total_with_sp=fields.Monetary(string="Totale Split Payment", store=True, readonly=True, compute=calcTotal)
    
    
    def _amount_all(self):
       res = super(SaleOrder, self)._amount_all()
       # do the things here
    
       if(self.partner_id.property_account_position_id.name == "Split Payment"):
            for record in self:
                record.amount_total=record.split_payment+record.total_with_sp
       return res
    
