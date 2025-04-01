
from django.urls import path
from .views import RegisterView, LoginView, ArticleListView,  LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('logout/',LogoutView.as_view(),name = "logout")
]

