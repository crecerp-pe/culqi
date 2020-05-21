# -*- coding: utf-'8' "-*-"
from odoo import models, fields, api

class AcquirerCulqi(models.Model):
    _inherit = 'payment.acquirer'
    provider = fields.Selection(selection_add=[('culqi', 'Culqi')])
    culqi_client_id = fields.Char('Culqi Client Id', size=256)
    culqi_secret_key = fields.Char('Culqi Secret Key', size=256)

