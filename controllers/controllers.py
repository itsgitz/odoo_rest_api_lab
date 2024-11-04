# -*- coding: utf-8 -*-
import json
import logging

from odoo import http

_logger = logging.getLogger(__name__)

class OdooRestApiLab(http.Controller):
    @http.route('/api/hello', auth='public', methods=['GET'])
    def index(self, **kw):
        data = {
            'message': 'hello from odoo api!'
        }

        _logger.info('response data: %s', data)

        return http.Response(
            json.dumps(data),
            status=200,
            mimetype='application/json' 
        )

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

