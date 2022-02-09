from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError
from django.http import HttpResponseServerError

from raterprojectapi.models import Category

class CategoryView(ViewSet):
    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","label")