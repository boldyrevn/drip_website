from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/categories.html')
def show_categories(cat_slug: str = ''):
    categories = Category.objects.all()
    return {'selected_category': cat_slug, 'categories': categories}
