from django.urls import path
from .views import *
urlpatterns=[
  path('signUp/',signUpView,name='signUp'),
  path('login/',loginView,name='login'),
  path('',homeView,name='home'),
]