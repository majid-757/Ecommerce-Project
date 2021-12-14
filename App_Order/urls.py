from django.urls import path
from .views import add_to_cart, card_view


app_name = 'App_Order'


urlpatterns = [
    path('add/<pk>/', add_to_cart, name='add'),
    path('cart/', card_view, name='cart'),

]


