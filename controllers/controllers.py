# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentCulqi(http.Controller):
#     @http.route('/payment_culqi/payment_culqi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_culqi/payment_culqi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_culqi.listing', {
#             'root': '/payment_culqi/payment_culqi',
#             'objects': http.request.env['payment_culqi.payment_culqi'].search([]),
#         })

#     @http.route('/payment_culqi/payment_culqi/objects/<model("payment_culqi.payment_culqi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_culqi.object', {
#             'object': obj
#         })
