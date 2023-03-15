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
from .views import BookViewSet, BookReadViewSet, UserViewSet, UserRecommendViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'book_read', BookReadViewSet)
router.register(r'user_recommend', UserRecommendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
