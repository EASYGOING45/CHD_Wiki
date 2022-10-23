from django.urls import path
from .views import user

app_name = 'wiki'
urlpatterns = [
    path('', user.index, name='index'),
]