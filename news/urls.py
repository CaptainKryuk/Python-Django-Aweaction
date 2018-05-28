from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.all_news, name='all_views'),
    path('article/<int:news_id>/', views.article, name='article'),
    url(r'^(?P<post_id>\d+)/share/$', views.test, name='post_share'),

]

