# -*- coding: utf-8 -*-
# from odoo import http


# class AbcRegistroIva(http.Controller):
#     @http.route('/abc_registro_iva/abc_registro_iva/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_registro_iva/abc_registro_iva/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_registro_iva.listing', {
#             'root': '/abc_registro_iva/abc_registro_iva',
#             'objects': http.request.env['abc_registro_iva.abc_registro_iva'].search([]),
#         })

#     @http.route('/abc_registro_iva/abc_registro_iva/objects/<model("abc_registro_iva.abc_registro_iva"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_registro_iva.object', {
#             'object': obj
#         })
