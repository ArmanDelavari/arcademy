from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('contact', views.contactpage, name='contactpage')
]