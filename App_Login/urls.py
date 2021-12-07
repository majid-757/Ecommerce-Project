from django.urls import path
from .views import sign_up, login_user, logout_user, user_profile


app_name = 'App_Login'


urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', user_profile, name='profile'),

]









