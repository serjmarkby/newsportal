from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post
import django.forms


# создаём фильтр
class NewsFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gte',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться
    # (т. е. подбираться) информация о товарах

    class Meta:
        model = Post

        # поля, которые мы будем фильтровать(т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
            'author': ['exact'],
            'postCategory': ['exact'],
            'rating': ['gt'],
        }
