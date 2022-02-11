from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='post'),
    path('create/', NewsCreate.as_view(), name='news_create'),
]