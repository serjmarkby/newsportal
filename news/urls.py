from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate, SearchList, NewsUpdate, NewsDelete


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='post'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('search/', SearchList.as_view(), name='search'),
    path('update/', NewsUpdate.as_view(), name='news_create'),
    path('delete/', NewsDelete.as_view(), name='news_delete'),
]