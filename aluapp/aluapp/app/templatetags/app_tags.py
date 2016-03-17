from django.template import Library

register = Library()

@register.filter
def as_range(value):
    return range(value)
