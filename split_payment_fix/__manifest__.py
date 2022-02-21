# -*- coding: utf-8 -*-
{
    'name': "ABC - split_payment_fix",

    'summary': """
        Modulo che risolve alcuni bug riscontrati nel modulo OCA split_payment. """,

    'description': """
        Modulo che risolve alcuni bug riscontrati nel modulo OCA split_payment.
    """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'l10n_it_withholding_tax','sale'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        
    ],
    "installable": True,
    # only loaded in demonstration mode
    'demo': [],
}
