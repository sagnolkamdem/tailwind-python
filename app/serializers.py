from rest_framework import serializers

from core.models import Announce, Comment, Category, Logement, Visit, Location


class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LogementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logement
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
