from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'auth'

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain-token'),
]
