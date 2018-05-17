from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Downloading projects
    path('downloading/', views.downloading, name='downloading'),

    # Editing profile settings
    path('edit/', views.edit, name='edit'),
    path('edit/password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('edit/password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('edit/additional_info/', views.edit_additional_info, name='edit_additional_info'),
    path('edit/additional_info/done/', views.edit_additional_info_done, name='edit_additional_info_done'),
]