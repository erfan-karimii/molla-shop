from django import template
from product.models import Product

register = template.Library()

@register.filter
def filter_show(value):
    return value.filter(is_show=True)

@register.filter
def show_count(value):
    return value.filter(is_show=True).count()

@register.filter
def right_px(value):
    flag = 0
    while value.parent:
        flag += 1
        value = value.parent
    return (flag + 2) * 20