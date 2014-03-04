from django import template
import re

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})