from django.urls import path
from . import views
from django.shortcuts import render

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('register/', views.register, name='register'),
# ]
#
#
# def home(request):
#     return render(request, 'home.html')

from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
