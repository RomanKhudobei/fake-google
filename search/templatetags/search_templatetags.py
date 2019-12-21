from django import template

register = template.Library()


@register.filter
def replace_foot_static(tag):
    tag = tag.replace('background:url(/images/nav_logo299.png)', 'background:url(/static/nav_logo299.webp)')
    tag = tag.replace('background:url(/images/nav_logo299.webp)', 'background:url(/static/nav_logo299.webp)')
    return tag
