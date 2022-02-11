from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator

from .models import Author, Post, PostCategory, Comment, Category
from .filters import NewsFilter
from .forms import NewsForm

# Create your views here.


class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в
    # котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')  # задаем фильтрацию для отображения - последняя новость вверху
    paginate_by = 9  # пагинация - сколько объектов будет на 1 странице
    form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст

        context['form'] = NewsForm()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    form_class = NewsForm

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = NewsForm()
        return context


class NewsCreate(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    # queryset = Post.objects.all()

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)  # создаем новую форму, забивая в неё данные из POST запроса
    #
    #     if form.is_valid():
    #         form.save()
    #     return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.


# дженерик для редактирования новости
class NewsUpdate(UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию
    # об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDelete(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


