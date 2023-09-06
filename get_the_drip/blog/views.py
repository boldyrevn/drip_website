from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.forms import UserCreationForm

from .forms import PublicationForm, RegisterUserForm
from .models import Publication, Category

header_links = [
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Suggest publication', 'url_name': 'add_pub'},
    {'title': 'Feedback', 'url_name': 'feedback'}
]


class ViewMixin:
    def make_context_data(self, **kwargs):
        context = dict()
        context['title'] = kwargs['title']
        context['header_links'] = header_links
        context['categories'] = Category.objects.raw("""
            SELECT bc.id, "name" FROM blog_category bc
            JOIN blog_publication ON blog_publication.cat_id = bc.id
            WHERE blog_publication.is_published = TRUE
            GROUP BY bc.id, "name"
            HAVING COUNT(blog_publication.id) > 0
        """)
        if 'selected_category' not in kwargs:
            context['selected_category'] = None
        else:
            context['selected_category'] = kwargs['selected_category']
        return context


class BlogHome(ViewMixin, ListView):
    paginate_by = 3
    model = Publication
    template_name = 'blog/index.html'
    context_object_name = 'publications'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.make_context_data(title='Get the DRIP',
                                              selected_category='')
        return context | user_context

    def get_queryset(self):
        return Publication.objects.filter(is_published=True)


class PublicationCategory(ViewMixin, ListView):
    model = Publication
    context_object_name = 'publications'
    template_name = 'blog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.make_context_data(title='Category',
                                              selected_category=self.kwargs["cat_slug"])
        return context | user_context

    def get_queryset(self):
        return Publication.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'])


class ShowPublication(ViewMixin, DetailView):
    model = Publication
    context_object_name = 'p'
    slug_url_kwarg = 'pub_slug'
    template_name = 'blog/publication.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.make_context_data(title=context['p'].title, selected_category=context['p'].cat.slug)
        return context | user_context


class AddPublication(ViewMixin, CreateView):
    form_class = PublicationForm
    template_name = 'blog/add_pub.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.make_context_data(title='Suggest publication')
        return context | user_context


class About(View, ViewMixin):
    def get(self, request, *args, **kwargs):
        context = self.make_context_data(title='About DRIP')
        return render(request, 'blog/about.html', context=context)


class Register(ViewMixin, CreateView):
    template_name = "blog/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.make_context_data(title="Register")
        return context | user_context


def feedback_page(request: HttpRequest):
    return HttpResponse("Come on, bitch, say it right to my face!")


def login_page(request: HttpRequest):
    return HttpResponse("Who fuck are you?")
