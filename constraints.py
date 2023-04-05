#   addons/maintenance/mantenance.py:L200
  _sql_constraints = [
        ('serial_no', 'unique(serial_no)', "Another asset already exists with this serial number!"),
    ]
           
#     addons/base/models/res_partner.py:L440
    @api.constrains('barcode')
    def _check_barcode_unicity(self):
        if self.barcode and self.env['res.partner'].search_count([('barcode', '=', self.barcode)]) > 1:
            raise ValidationError('An other user already has this barcode')                
