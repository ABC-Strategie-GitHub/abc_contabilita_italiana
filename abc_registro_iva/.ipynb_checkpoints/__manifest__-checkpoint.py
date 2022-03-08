# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_registro_iva",

    'summary': """ Modulo che personalizza il template del Registro IVA standard di Odoo aggiungendo la colonna Data competenza IVA e modificando il NUM. FATT. in N. DOCUMENTO agganciato al campo move.ref della fattura. """,

    'description': """ Modulo che personalizza il template del Registro IVA standard di Odoo aggiungendo la colonna Data competenza IVA e modificando il NUM. FATT. in N. DOCUMENTO agganciato al campo move.ref della fattura. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Account',
    'version': '0.1',

    'depends': ['base', 'account', 'l10n_it_vat_registries', 'base_setup', 'l10n_it_account', 'web', 'account_tax_balance', 'date_range', 'l10n_it_vat_settlement_date'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/registro_iva_formato_carta.xml',
        'report/registro_iva.xml',
        'report/registro_iva_print_report.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
