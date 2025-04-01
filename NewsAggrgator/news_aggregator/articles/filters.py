# filepath: /f:/BTES Training/Module 3 (Back End)/NewsAggrgator/NewsAggrgator/news_aggregator/articles/filters.py
import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }