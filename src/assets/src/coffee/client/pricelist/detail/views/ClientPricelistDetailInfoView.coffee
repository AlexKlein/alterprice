$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Switcher = require 'base/utils/Switcher'


module.exports = class ClientPricelistDetailInfoView extends Marionette.ItemView
    el: $('#client-pricelist-detail-info-view')

    template: false

    ui:
        switcher: '.switcher-wrapper'


    initialize: (options) =>
        @channel = options.channel
        new Switcher @$(@ui.switcher)