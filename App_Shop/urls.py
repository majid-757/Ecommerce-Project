from django.urls import path
from .views import Home


app_name = 'App_Shop'


urlpatterns = [
    path('', Home.as_view(), name='home'),
]









