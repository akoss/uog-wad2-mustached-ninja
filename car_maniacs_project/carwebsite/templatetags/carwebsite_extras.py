from django import template
from carwebsite.models import Manufacturer

register = template.Library()

@register.inclusion_tag('carwebsite/mans.html')
def get_manufacturer_list(man=None):
    return {'mans': Manufacturer.objects.order_by('name'), 'act_man': man}