# -*- coding: utf-8 -*-
{
    'name': "Fattura Immediata",

    'summary': """
        Modulo per la creazione e stampa di una fattura immediata""",

    'description': """
        Modulo per la creazione e stampa di una fattura immediata
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'sale',
                'stock',
                'partner_fax',
                'abc_codice_arca',
                'abc_codice_iva',
                'abc_x_planethoreca',
                'l10n_it_account',
                'l10n_it_delivery_note',
                'l10n_it_delivery_note_base',
                'l10n_it_delivery_note_batch',
                'l10n_it_delivery_note_order_link',
                'l10n_it_fatturapa',
                'l10n_it_fatturapa_in',
                'l10n_it_fatturapa_out',
                'l10n_it_fatturapa_sale',
                'l10n_it_fiscal_document_type',
                'l10n_it_fiscal_payment_term',
                'l10n_it_fiscalcode',
                'l10n_it_payment_reason',
                'l10n_it_pec',
                'l10n_it_rea',
                'l10n_it_split_payment',
               ],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/fattura_paperformat.xml',
        'report/report_fattura_immediata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
