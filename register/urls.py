from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='register/login.html'),  name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home, name='home'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('list_of_users/', views.list_of_users, name='list_of_users')
]
