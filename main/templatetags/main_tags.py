import bleach
from django import template

register = template.Library()

@register.filter
def bleach_xss(value):
    return bleach.clean(value)


@register.filter
def bleach_linkify(value):
    return bleach.clean(value)
