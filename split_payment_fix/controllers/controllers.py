# -*- coding: utf-8 -*-
# from odoo import http


# class SplitPaymentFix(http.Controller):
#     @http.route('/split_payment_fix/split_payment_fix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/split_payment_fix/split_payment_fix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('split_payment_fix.listing', {
#             'root': '/split_payment_fix/split_payment_fix',
#             'objects': http.request.env['split_payment_fix.split_payment_fix'].search([]),
#         })

#     @http.route('/split_payment_fix/split_payment_fix/objects/<model("split_payment_fix.split_payment_fix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('split_payment_fix.object', {
#             'object': obj
#         })
