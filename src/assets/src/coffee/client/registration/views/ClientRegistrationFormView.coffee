$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'
Select = require 'base/utils/Select'
Checkbox = require 'base/utils/Checkbox'
require 'jquery-maskedinput'


module.exports = class ClientRegistrationFormView extends Marionette.ItemView
    el: $('#client-registration-form-view')

    template: false

    ui:
        form: '#registration-form'
        radioWrapper: '.radio-wrapper'
        phoneInput: '.phone-mask'
        selectWrapper: '.select'
        checkboxWrapper: 'label.checkbox'


    initialize: (options) =>
        @channel = options.channel
        new Radio @$(@ui.radioWrapper)
        new Form {form: @$(@ui.form), dataType: 'html'}
        @$(@ui.phoneInput).mask('(999) 999-9999')
        new Select @$(@ui.selectWrapper)
        Checkbox.init @$(@ui.checkboxWrapper)