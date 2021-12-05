from django.urls import path
from .views import sign_up


app_name = 'App_Login'


urlpatterns = [
    path('signup/', sign_up, name='signup'),
    
]









