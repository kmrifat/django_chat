from django.urls import path

from authentication.views.auth_view import *
from rest_framework.authtoken import views

from authentication.views.message_view import MessageView
from config import settings

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('registration/', RegisterView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('users/', UsersView.as_view()),
    path('message/', MessageView.as_view()),
    path('test-socket/', test_socket)
]
