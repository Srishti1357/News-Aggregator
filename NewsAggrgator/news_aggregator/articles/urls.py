
from django.urls import path
from .views import RegisterView, LoginView, ArticleListView,  LogoutView, save_article, get_saved_articles, remove_saved_article, ArticleFilteredNoPaginationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('logout/',LogoutView.as_view(),name = "logout"),

    path('save-article/<int:article_id>/', save_article, name='save_article'),
    path('saved-articles/', get_saved_articles, name='get_saved_articles'),
    path('remove-saved-article/<int:article_id>/', remove_saved_article, name='remove_saved_article'),
    path('articles/filter/', ArticleFilteredNoPaginationView.as_view()),

]

