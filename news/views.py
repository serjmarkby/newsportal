from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator

from .models import Author, Post, PostCategory, Comment, Category
from .filters import NewsFilter
from .forms import NewsForm

# Create your views here.


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 9
    form_class = NewsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст

        context['form'] = NewsForm
        return context


class NewsDetail(DeleteView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


