from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import datetime
from rest_framework.filters import SearchFilter


class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
