from django.forms import ModelForm, BooleanField
from .models import Post
from django.contrib.auth.models import User


# Создаём модельную форму
class NewsForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')  # добавляем галочку, или же true-false поле

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма
    # и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory', 'postPhoto']


# Создаём модельную форму
class UserForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')  # добавляем галочку, или же true-false поле

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма
    # и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']
