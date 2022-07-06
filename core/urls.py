from django.urls import path, include
from .views import double_list, double_create


urlpatterns = [
    path('', double_list, name='double_list'),
    path('double_create', double_create, name='double_create')
]
