from django.urls import path
from .views import register, loginauth, home, logoutauth


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', loginauth, name='login'),
    path('logout/', logoutauth, name='logout'),

]