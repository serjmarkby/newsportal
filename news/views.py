from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Author, Post, PostCategory, Comment, Category

# Create your views here.


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 9


class NewsDetail(DeleteView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


