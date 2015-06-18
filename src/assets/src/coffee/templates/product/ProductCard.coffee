PrettyPrice = require 'base/utils/PrettyPrice'

template = (locals) =>
    price = PrettyPrice.format locals.min_price

    return "<div class=\"item-card-block block-1-x first-inline\">
    <a href=\"/product/detail/#{locals.id}/\">
        <div class=\"image\" style=\"background-image: url(/static/dist/images/content/items/6.png)\"></div>
        <div class=\"title\">#{locals.name}</div>
    </a>
    <div class=\"price\">от <span>#{price}</span> руб</div>
    <div class=\"shop\">В <a href=\"#\">#{locals.offer.name}</a><br>ещё <a href=\"#\">#{locals.offers_count} предложений</a></div>
</div>"


module.exports = template