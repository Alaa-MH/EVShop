from django import template

register=template.Library()

@register.filter(name='concat')
def concat(value):
    return '/store/category/'+value.lower()+'/'