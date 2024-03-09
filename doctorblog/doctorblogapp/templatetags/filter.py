# filters.py
from django import template

register = template.Library()

@register.filter
def truncate_summary(value):
    words = value.split()[:15]
    if len(words) < 15:
        return ' '.join(words)
    else:
        return ' '.join(words) + '...'
