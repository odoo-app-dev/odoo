from odoo import models, fields, api, _
from datetime import datetime, timedelta
import pytz

  tz = self.env['ir.config_parameter'].sudo().get_param('sd_food.tz')  # Asia/Tehran
  
  time_z = pytz.timezone(tz or 'UTC')     # Asia/Tehran
  datetime.now()                          # 2022-12-20 07:02:17.357002
  datetime.now(time_z)                    # 2022-12-20 10:32:17.357020+03:30
  datetime.now(time_z).date()             # 2022-12-20

