Number = require 'base/utils/Number'

template = (locals) =>
    if locals.viewURL
        name = "<a href=\"#{locals.viewURL}\" target=\"_blank\">#{locals.category.name}</a>"
    else
        name = locals.category.name

    return "
        <td>#{name}</td>
        <td class=\"text-center\">#{locals.lead_price}</td>
        <td class=\"text-center\">
            <div class=\"number-input-wrapper\">
                <button type=\"button\" class=\"increment-btn btn\"></button>
                <input type=\"text\" class=\"number-input\" value=\"#{locals.price}\" />
                <button type=\"button\" class=\"decrement-btn btn\"></button>
            </div>
        </td>"


module.exports = template
