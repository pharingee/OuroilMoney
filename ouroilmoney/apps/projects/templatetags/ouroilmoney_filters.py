from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, 0)


@register.filter
def get_percentage(amount, total):
    return round((float(amount) / float(total)) * 100, 2)


@register.filter
def get_int(val):
    return int(val)


@register.filter
def remove_commas(val):
    try:
        return int(val.replace(',', ''))
    except AttributeError:
        return val


@register.filter
def is_equal(string, compare):
    print string, compare
    return True
