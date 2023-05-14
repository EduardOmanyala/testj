from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post1/Kenya-is-a-Country-in-East-Africa', views.storyone, name='blog-storyone'),
]
