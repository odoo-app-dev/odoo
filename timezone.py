from odoo import models, fields, api, _
from datetime import datetime, timedelta
import pytz

  tz = self.env['ir.config_parameter'].sudo().get_param('sd_food.tz')
  time_z = pytz.timezone(tz or 'UTC')
  datetime.today().date(time_z)
  datetime.now(time_z).hour > 14
