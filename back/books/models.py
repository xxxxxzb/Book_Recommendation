from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models


class DoubanBook(models.Model):
    id = models.IntegerField(primary_key=True)
    book_type = models.TextField()
    cover = models.TextField()
    title = models.TextField()
    country = models.TextField()
    author = models.TextField()
    translator = models.TextField()
    publisher = models.TextField()
    pub_date = models.TextField()
    price = models.TextField()
    ratting = models.FloatField()
    ratting_num = models.TextField()
    summary = models.TextField()

    class Meta:
        db_table = 'douban_book'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
