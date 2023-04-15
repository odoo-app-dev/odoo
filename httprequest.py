from odoo import http
from odoo.http import request
import json

class SdFoodContorller(http.Controller):

    @http.route('/sd_food/activate_devices/', auth="public", type='json', website=True, csrf=False)
    def activate_devices(self, **kwargs):
        data = json.loads(request.httprequest.data)
        print(data)
            # {"device_ids": []}

        print(request.httprequest.remote_addr)
            # 172.17.120.40
            
        print(request.httprequest.headers)
            # Host: star.oeid.ir
            # User-Agent: python-requests/2.28.2
            # Accept-Encoding: gzip, deflate
            # Accept: */*
            # Content-Type: application/json
            # X-Forwarded-Proto: https
            # X-Forwarded-For: 172.17.120.40
            # X-Forwarded-Host: star.oeid.ir
            # X-Forwarded-Server: star.oeid.ir
            # Content-Length: 14
            # Connection: close
        print(request.httprequest.url_root)
            #  https://star.oeid.ir/       
        print(request.httprequest.method)
            # POST
        print(request.session.sid)
            # e17d9271fcbf5671f8bd284146ed8c805fcdc917
  
