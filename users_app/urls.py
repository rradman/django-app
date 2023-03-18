from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('get_user/<username>', views.get_user, name='get_user'),
    path('save_user/', views.save_user, name='save_user'),
]
