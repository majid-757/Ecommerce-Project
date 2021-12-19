from django.urls import path
from .views import add_to_cart, card_view, remove_from_cart


app_name = 'App_Order'


urlpatterns = [
    path('add/<pk>/', add_to_cart, name='add'),
    path('cart/', card_view, name='cart'),
    path('remove/<pk>/', remove_from_cart, name='remove'),

]


