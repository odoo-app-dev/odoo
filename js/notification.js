odoo.define('sd_food.refresh_div', require => {
    'use strict';
    var FormController = require('web.FormController');
    var core = require('web.core');  // needed
    var _t = core._t; //needed

    var ExtendFormController = FormController.include({
    saveRecord: function() {
        if (this.modelName == 'sd_food.groups')
            this.displayNotification({ message: _t('This form is saved'), type: 'success', sticky: true,});   // needed
            // type:[success, danger, warning]
            // sticky: [false]-> disapear after 5 seconds [true]-> needed to be closed manualy.
        var res = this._super.apply(this, arguments);
        return res
        }

});
});
