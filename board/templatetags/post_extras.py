from django import template


register = template.Library()


@register.filter
def latest_comments(value):
    return value.comment_set.order_by('updated_at').reverse()[:3]
