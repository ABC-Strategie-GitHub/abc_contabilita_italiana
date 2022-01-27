# Copyright 2015  Davide Corio <davide.corio@abstract.it>
# Copyright 2015-2016  Lorenzo Battistini - Agile Business Group
# Copyright 2016  Alessio Gerace - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import UserError
from odoo.tools import float_compare
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"


    def set_receivable_line_ids(self):
        """Recompute all account move lines by _recompute_dynamic_lines()
        and set correct receivable lines
        """
        _logger.info('New Code Running')
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
