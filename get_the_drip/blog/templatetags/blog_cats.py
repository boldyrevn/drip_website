from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/categories.html')
def show_categories(cat_id: int = 0):
    categories = Category.objects.all()
    return {'selected_category': cat_id, 'categories': categories}
