from odoo import fields, models, api
import io
import base64
from PIL import Image
from odoo.tools.image import image_data_uri
from io import StringIO
import odoo
class MaintenanceExtendsModels(models.Model):
    _name = 'maintenance.models'
    _description = 'Products model names'

    name = fields.Char()
    width = fields.Float()
    depth = fields.Float()
    height = fields.Float()
    image = fields.Image()
    image_x = fields.Integer()
    image_y = fields.Integer()
    
    @api.onchange('image')
    def model_image_size(self):
        for rec in self:
            try:
                if rec.image[-2:] != '==':
                    padded_data = rec.image + b'=='
                else:
                    padded_data = rec.image
                image_file = base64.b64decode(padded_data)
                im = Image.open(io.BytesIO(image_file))
                rec.image_x = im.size[0]
                rec.image_y = im.size[1]
                # print(f'\n IMAGE: {padded_data[-2:]}')

            except Exception as e:
                rec.image_x = 0
                rec.image_y = 0
                # print(f'\n ERROR: {e}')
