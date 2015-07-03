$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientPricelistDetailProductsItemView = require './ClientPricelistDetailProductsItemView'
PricelistProductsTemplate = require 'templates/client/PricelistProducts'


module.exports = class ClientPricelistDetailProductsCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: PricelistProductsTemplate

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientPricelistDetailProductsItemView

    childViewOptions: (model, index) =>
        return {channel: @channel}
