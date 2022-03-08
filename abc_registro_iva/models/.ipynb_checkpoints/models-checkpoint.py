# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError

import time


from odoo.exceptions import UserError
from odoo.tools.misc import formatLang
from odoo.tools.translate import _

import logging
_logger = logging.getLogger(__name__)


class abc_registro_iva(models.Model):
    _name = 'abc_registro_iva.abc_registro_iva'
    _description = 'abc_registro_iva.abc_registro_iva'

# Eredito la classe che viene utilizzata per passare i parametri al report rinominandola con il nome del modulo attuale e il nuovo report stampa
# "report.abc_registro_iva.registro_iva_template".
class ReportRegistroIva(models.AbstractModel):
    _inherit = "report.l10n_it_vat_registries.report_registro_iva"
    _name = "report.abc_registro_iva.registro_iva_template"

# Eredito la classe che permette di stampare il Registro IVA sovrascrivendo alla fine il ritorno con il nuovo report "abc_registro_iva.registro_iva_print_report".
class WizardRegistroIva(models.TransientModel):
    _inherit = "wizard.registro.iva"
    _name = "wizard.registro.iva"
  
    def print_registro(self):
        self.ensure_one()
        wizard = self
        if not wizard.journal_ids:
            raise UserError(
                _(
                    "No journals found in the current selection.\n"
                    "Please load them before to retry!"
                )
            )
        move_ids = self._get_move_ids(wizard)

        datas_form = {}
        datas_form["from_date"] = wizard.from_date
        datas_form["to_date"] = wizard.to_date
        datas_form["journal_ids"] = [j.id for j in wizard.journal_ids]
        datas_form["fiscal_page_base"] = wizard.fiscal_page_base
        datas_form["registry_type"] = wizard.layout_type
        datas_form["year_footer"] = wizard.year_footer

        lang_code = self.env.company.partner_id.lang
        lang = self.env["res.lang"]
        lang_id = lang._lang_get(lang_code)
        date_format = lang_id.date_format
        datas_form["date_format"] = date_format

        if wizard.tax_registry_id:
            datas_form["tax_registry_name"] = wizard.tax_registry_id.name
        else:
            datas_form["tax_registry_name"] = ""
        datas_form["only_totals"] = wizard.only_totals
        # report_name = 'l10n_it_vat_registries.report_registro_iva'
        report_name = "abc_registro_iva.registro_iva_print_report"
        datas = {"ids": move_ids, "model": "account.move", "form": datas_form}
        return self.env.ref(report_name).report_action(self, data= datas)