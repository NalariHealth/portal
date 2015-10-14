from django.template import Library

register = Library()

@register.filter(name='lookup')
def lookup(d, key):
	return d[key]