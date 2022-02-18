# -*- coding: utf-8 -*-
# from odoo import http


# class AbcDeliveryNoteFix(http.Controller):
#     @http.route('/abc_delivery_note_fix/abc_delivery_note_fix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_delivery_note_fix/abc_delivery_note_fix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_delivery_note_fix.listing', {
#             'root': '/abc_delivery_note_fix/abc_delivery_note_fix',
#             'objects': http.request.env['abc_delivery_note_fix.abc_delivery_note_fix'].search([]),
#         })

#     @http.route('/abc_delivery_note_fix/abc_delivery_note_fix/objects/<model("abc_delivery_note_fix.abc_delivery_note_fix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_delivery_note_fix.object', {
#             'object': obj
#         })
