# -*- coding: utf-8 -*-

import datetime
import logging
_logger = logging.getLogger(__name__)


from odoo import models, fields, api

DONE_READONLY_STATE = {"done": [("readonly", True)]}

#Eredito il modulo sale.order per modificare la funzione che genera le fatture
class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        colli = 0
        peso_spedizione = 0
        peso_netto = 0
        volume = 0
        vettore_id = False
        for pick in self.picking_ids:
            if pick.location_dest_id.usage=='customer':
                if pick.carrier_id.id:
                    vettore_id = pick.carrier_id.id
                for collo in pick.package_ids:
                    colli = colli + 1
                    peso_netto += collo.weight
                    if (collo.shipping_weight!=0):
                        peso_spedizione += collo.shipping_weight
                    else:
                        peso_spedizione += peso_netto
                    #VERIFICA SE E COMPILATA LA TIPOLOGIA DEL COLLO E NE RICAVA IL VOLUME
                    if (collo.packaging_id.id):
                        #uom = collo.packaging_id.length_uom_name
                        altezza = collo.packaging_id.height
                        larghezza = collo.packaging_id.width
                        lunghezza = collo.packaging_id.packaging_length
                        volume += altezza * larghezza * lunghezza
                    
                
            
        res = super()._prepare_invoice()
        res['packages'] = colli
        res['volume'] = volume
        res['gross_weight'] = peso_spedizione
        res['net_weight'] = peso_netto
        res['volume_uom_id'] = self.env.ref("uom.product_uom_cubic_meter", raise_if_not_found=False)
        res['carrier_id'] = vettore_id
        return res



#Eredito il modulo account.move per accedervi e creare i nuovi campi.
class accountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"
    
    def _default_volume_uom(self):
        return self.env.ref("uom.product_uom_litre", raise_if_not_found=False)

    def _domain_volume_uom(self):
        uom_category_id = self.env.ref(
            "uom.product_uom_categ_vol", raise_if_not_found=False
        )

        return [("category_id", "=", uom_category_id.id)]

    def _default_weight_uom(self):
        return self.env.ref("uom.product_uom_kgm", raise_if_not_found=False)

    def _domain_weight_uom(self):
        uom_category_id = self.env.ref(
            "uom.product_uom_categ_kgm", raise_if_not_found=False
        )

        return [("category_id", "=", uom_category_id.id)]
  
    def update_transport_datetime(self):
        self.transport_datetime = datetime.datetime.now()
        
    
    '''default_transport_condition_id = fields.Many2one(
        "stock.picking.transport.condition", string="Condizione di trasporto"
    )
    default_goods_appearance_id = fields.Many2one(
        "stock.picking.goods.appearance", string="Aspetto dei beni"
    )
    default_transport_reason_id = fields.Many2one(
        "stock.picking.transport.reason", string="Causale di trasporto"
    )
    default_transport_method_id = fields.Many2one(
        "stock.picking.transport.method", string="Metodo di trasporto"
    )'''
    
    carrier_id = fields.Many2one(
        "res.partner",
        string="Vettore",
        #states=DONE_READONLY_STATE,
        tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    
    transport_condition_id = fields.Many2one(
        "stock.picking.transport.condition",
        string="Condizione di trasporto",
        #states=DONE_READONLY_STATE,
    )
    goods_appearance_id = fields.Many2one(
        "stock.picking.goods.appearance",
        string="Aspetto dei beni",
        #states=DONE_READONLY_STATE,
    )
    transport_reason_id = fields.Many2one(
        "stock.picking.transport.reason",
        string="Causale di trasporto",
        #states=DONE_READONLY_STATE,
    )
    transport_method_id = fields.Many2one(
        "stock.picking.transport.method",
        string="Metodo di trasporto",
        #states=DONE_READONLY_STATE,
    )
    
    note = fields.Html(string="Note interne")
    
    packages = fields.Integer(string="Colli")
    volume = fields.Float(string="Volume")
    
    volume_uom_id = fields.Many2one(
        "uom.uom",
        string="Volume UdM",
        default=_default_volume_uom,
        domain=_domain_volume_uom,
        #states=DONE_READONLY_STATE,
    )
    gross_weight = fields.Float(string="Peso Lordo")
    gross_weight_uom_id = fields.Many2one(
        "uom.uom",
        string="Peso Lordo UdM",
        default=_default_weight_uom,
        domain=_domain_weight_uom,
        #states=DONE_READONLY_STATE,
    )
    net_weight = fields.Float(string="Peso Netto")
    net_weight_uom_id = fields.Many2one(
        "uom.uom",
        string="Peso Netto UdM",
        default=_default_weight_uom,
        domain=_domain_weight_uom,
        #states=DONE_READONLY_STATE,
    )
    transport_datetime = fields.Datetime(
        string="Data/Ora del trasporto"
    )
    
    cod_lista = fields.Char(
        string="Cod. Lista"
    )
                            
    #DEPRECATO I DATI DI TRASPORTO VENGONO COMPILATI CON I DATI DELLA CONSEGNA QUANDO SI GENERA LA FATTURA DALL ORDINE DI VENDITA
    #@api.onchange('invoice_line_ids')
    #def _onchange_invoice_line_ids(self):
    #    for line in self.invoice_line_ids:
    #        _logger.info('LINE Create a %s with vals %s', self._name, line.name)
    #        _logger.info('DDT Create a %s with vals %s', self._name, line.delivery_note_id)
    #        _logger.info('SALE Create a %s with vals %s', self._name, line.sale_line_ids)
    #    super()._onchange_invoice_line_ids()
        
                            


# class fattura_immediata(models.Model):
#     _name = 'fattura_immediata.fattura_immediata'
#     _description = 'fattura_immediata.fattura_immediata'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
