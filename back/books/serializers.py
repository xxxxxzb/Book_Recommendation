from rest_framework import serializers
from .models import DoubanBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubanBook
        fields = '__all__'
