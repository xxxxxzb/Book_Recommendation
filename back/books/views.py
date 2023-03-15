from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import DoubanBook, Users, UserRecommend, BookRead
from rest_framework import viewsets
from .serializers import BookSerializer, UsersSerializer, UserRecommendSerializer, BookReadSerializer
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = DoubanBook.objects.all().order_by('id')[:1000]
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class BookReadViewSet(viewsets.ModelViewSet):
    queryset = BookRead.objects.all()
    serializer_class = BookReadSerializer


class UserRecommendViewSet(viewsets.ModelViewSet):
    queryset = UserRecommend.objects.all()
    serializer_class = UserRecommendSerializer

# @api_view(['GET'])
# def book_list(request):
#     books = DoubanBook.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

#
# def index(request):
#     douban_book = DoubanBook.objects.all()[:10]
#     context = {'douban_book': douban_book}
#     return render(request, 'books/index.html', context)
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = UserLoginForm()
#     return render(request, 'login.html', {'form': form})
#
#
# def logout(request):
#     return redirect('home')
#
#
# def home(request):
#     return render(request, 'home.html')
