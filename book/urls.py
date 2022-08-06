from .views import main,done,index,dashboard
from django.urls import path

urlpatterns = [
    path("", main, name='main'),
    path('done/',done,name='done'),
    path('main/',index, name = 'index'),
    path('dash/',dashboard, name = 'dashboard')
]
