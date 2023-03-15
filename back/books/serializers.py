from rest_framework import serializers
from .models import DoubanBook, Users, BookRead, UserRecommend


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubanBook
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRead
        fields = '__all__'


class UserRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecommend
        fields = '__all__'
