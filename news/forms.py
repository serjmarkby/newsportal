from django.forms import ModelForm, BooleanField
from .models import Post, Author
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Создаём модельную форму
class NewsForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')  # добавляем галочку, или же true-false поле

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма
    # и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory', 'postPhoto']


class UserForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']

