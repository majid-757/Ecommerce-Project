from django.urls import path

from .views import checkout

app_name = 'App_Payment'


urlpatterns = [
    path('checkout', checkout, name='checkout'),

]








