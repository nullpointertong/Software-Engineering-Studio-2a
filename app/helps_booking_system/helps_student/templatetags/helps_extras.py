from django import template

register = template.Library()

@register.filter
def subtract(value, arg) -> int:
    return int(value) - int(arg)

@register.filter
def add(value, arg) -> int:
    return int(value) + int(arg)

@register.filter
def multiply(value, arg) -> int:
    return int(value) * int(arg)

@register.filter
def divide(value, arg) -> int:
    return int(value) / int(arg)
