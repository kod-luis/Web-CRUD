from django.urls import path
from .views import *

urlpatterns = [
    path('', listapet, name='index'),
    path('<int:pk>/', saveform, name='info'),
    path('add', saveform, name='add'),
    path('del/<int:pk>/', deletapet, name='del'),
]
