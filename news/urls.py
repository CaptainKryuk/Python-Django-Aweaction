from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_news, name='all_views'),
    path('article/<int:news_id>/', views.article, name='article'),
]
