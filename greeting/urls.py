from django.urls import path
from .views import hello_user, register, secretcode, custom_logout
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", hello_user),
    path('register/', register, name='registration'),
    path('login/', LoginView.as_view(template_name='greeting/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('secretpanel/', secretcode, name='secretpanel' ),
    path('logout/', custom_logout, name='custom_logout'),
]