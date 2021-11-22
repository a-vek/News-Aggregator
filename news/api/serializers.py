from news.models import Headline
from rest_framework import serializers


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['name', 'desc', 'url', 'category']
