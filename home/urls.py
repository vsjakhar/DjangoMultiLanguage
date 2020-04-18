from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'home'

urlpatterns = [
	path('', home, name='home'),
]