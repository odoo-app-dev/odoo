from odoo import http
from odoo.http import request
import logging

class SdWbsite(http.Controller):
    @http.route('/sd_website/sd/', type='http', auth="public", website=True)
    def sd_index(self, **kwargs):
      context = request.env.context
      logging.log(context.get('uid'))
