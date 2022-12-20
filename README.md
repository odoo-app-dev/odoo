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
