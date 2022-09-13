from django import template
import re

register=template.Library()

@register.filter(name='concat')
def concat(value):
    return '/store/category/'+value.lower()+'/'
