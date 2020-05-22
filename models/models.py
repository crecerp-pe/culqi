# -*- coding: utf-'8' "-*-"

from odoo import api, fields, models, _
from odoo.addons.payment.models.payment_acquirer import ValidationError

class AcquirerCulqi(models.Model):
    _inherit = 'payment.acquirer'
    provider = fields.Selection(selection_add=[('culqi', 'Culqi')])
    culqi_client_id = fields.Char('Culqi Client Id', size=256)
    culqi_secret_key = fields.Char('Culqi Secret Key', size=256)


    def culqi_form_generate_values(self,values):
    	print('generate values')
    	culqi_tx_values = dict(values)
    	return culqi_tx_values

    def _get_culqi_urls(self, enviroment):
    	if enviroment== 'prod':
    		return {
    			culqi_form_url : 'https://www.culqi.com/mla/checkout/pay'
    			culqi_rest_url : 'https://api.culqi.com/oauth/token'
    		}
    	else:
    		return {
    			culqi_form_url : 'https://sandbox.culqi.com/mla/checkout/pay'
    			culqi_rest_url : 'https://api.sandbox.culqi.com/oauth/token'
    		}

    def culqi_get_form_action_url(self):
    	self._get_culqi_urls(self.enviroment)['culqi_form_url']