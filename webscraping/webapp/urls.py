from django.urls import path
from webapp.views import *
urlpatterns = [
    path('',index,name='index'),
]
