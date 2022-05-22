from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index),
    path('board/<int:id>', board),
    path('board/<int:id>/result', result),
    path('boardForm/',boardForm),
    path('problem/add',add),
]