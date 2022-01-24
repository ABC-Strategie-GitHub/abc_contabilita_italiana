# -*- coding: utf-8 -*-
# from odoo import http


# class FatturaImmediata(http.Controller):
#     @http.route('/fattura_immediata/fattura_immediata/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fattura_immediata/fattura_immediata/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fattura_immediata.listing', {
#             'root': '/fattura_immediata/fattura_immediata',
#             'objects': http.request.env['fattura_immediata.fattura_immediata'].search([]),
#         })

#     @http.route('/fattura_immediata/fattura_immediata/objects/<model("fattura_immediata.fattura_immediata"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fattura_immediata.object', {
#             'object': obj
#         })
