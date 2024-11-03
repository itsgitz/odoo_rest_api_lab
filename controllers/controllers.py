# -*- coding: utf-8 -*-
# from odoo import http


# class OdooRestApiLab(http.Controller):
#     @http.route('/odoo_rest_api_lab/odoo_rest_api_lab', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_rest_api_lab/odoo_rest_api_lab/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_rest_api_lab.listing', {
#             'root': '/odoo_rest_api_lab/odoo_rest_api_lab',
#             'objects': http.request.env['odoo_rest_api_lab.odoo_rest_api_lab'].search([]),
#         })

#     @http.route('/odoo_rest_api_lab/odoo_rest_api_lab/objects/<model("odoo_rest_api_lab.odoo_rest_api_lab"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_rest_api_lab.object', {
#             'object': obj
#         })

