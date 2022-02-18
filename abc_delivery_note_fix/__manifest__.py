# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_delivery_note_fix",

    'summary': """ Modulo che risolve il problema relativo alla creazione dei DDT senza ordine che dava errore. """,

    'description': """ Modulo che risolve il problema relativo alla creazione dei DDT senza ordine che dava errore. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Fix',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'delivery', 'l10n_it_delivery_note_base', 'l10n_it_delivery_note'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
