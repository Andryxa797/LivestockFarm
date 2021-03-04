from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from data.models import DataBeforeProcess


class DataBeforeProcessSerializer(ModelSerializer):
    user = serializers.StringRelatedField()  # Позволяет записывать имя не как int, а как строку

    class Meta:
        model = DataBeforeProcess
        fields = '__all__'
