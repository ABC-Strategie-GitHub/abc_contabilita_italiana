# -*- coding: utf-8 -*-
{
    'name': "ABC - Fattura Immediata",

    'summary': """
        Modulo per la creazione e stampa di una fattura immediata.""",

    'description': """
        Modulo per la creazione e stampa di una fattura immediata.
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale','l10n_it_delivery_note',
                'l10n_it_delivery_note_base',
                'l10n_it_delivery_note_batch',
                'l10n_it_delivery_note_order_link'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/fattura_paperformat.xml',
        'report/report_fattura_immediata.xml',
    ],
    "installable": True,
    "application": True,
    # only loaded in demonstration mode
    'demo': [],
}
