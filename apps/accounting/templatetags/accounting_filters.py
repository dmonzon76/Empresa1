from django import template

register = template.Library()

@register.filter
def split(value, separator="."):
    return value.split(separator)

@register.filter
def mul(value, arg):
    """Multiplica value * arg en templates."""
    try:
        return float(value) * float(arg)
    except:
        return ""
