from django.urls import path
from . import views

app_name = 'hook'

urlpatterns = [
    path('',views.index, name = 'index'),
]