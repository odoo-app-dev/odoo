# odoo
While developing odoo apps, sometimes it neened to have some minor changes in odoo core. I add them here it might be usefull for other developers.

## wesite
#### find out which user is loged in 
 [website_check_user_id.py](website_check_user_id.py)
 
## survey
#### To add page break while printing survey results
addons/survey/views/survey_templates_statistics.xml#L64
            <p style="page-break-after: always;"></p>
https://github.com/odoo-app-dev/odoo/blob/afb2862e59bb83b66a73ccc49f09ab1beff11a60/survey_templates_statistics.xml#L64

## Javascript
#### Notification
https://github.com/odoo-app-dev/odoo/blob/main/js/notification.js

## Pyton

#### Constrains
[Sample 1](https://github.com/odoo/odoo/blob/2242ec58e3ede51ae40879aedc3a8179d0d4ae49/addons/maintenance/models/maintenance.py#L198)
[Sample 2](https://github.com/odoo/odoo/blob/8b16d691d810b3dcfb3b3bac7a868aeb180c51b5/odoo/addons/base/models/res_partner.py#L441)

#### field.Selection
state = field.Selection([('a', 'Firest'),('b', 'Second')])

- record.state => a
- dict(record._fields["state"].selection).get(record.state) => First
- dict(record._fields["state"]._description_selection(record.env)).get(record.state)  => First ( translatable in website + 
[Explicit exports](https://www.odoo.com/documentation/16.0/developer/howtos/translations.html#explicit-exports))

### Get the current record id on creation
```
def create(self, vals):
    res = super(<class name>, self).create(vals)
    print('Record ID: ', res.id)
    return res
```
