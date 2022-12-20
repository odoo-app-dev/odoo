odoo.define('sd_food.refresh_div', require => {
    'use strict';
    var FormController = require('web.FormController');
    var core = require('web.core');
    var _t = core._t;

    var ExtendFormController = FormController.include({
    saveRecord: function() {
        if (this.modelName == 'sd_food.groups')
            this.displayNotification({ message: _t('This form is saved'), type: 'success', sticky: true,});   // success, danger, warning
        var res = this._super.apply(this, arguments);
        return res
        }

});
});
