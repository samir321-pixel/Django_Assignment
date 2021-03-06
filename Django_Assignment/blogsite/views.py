from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer


class BlogViewsets(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, ]
    search_fields = ['category__name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user, active=True)
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=401)

    def list(self, request, *args, **kwargs):
        query = Blog.objects.all().order_by('-created_at')
        query = self.filter_queryset(self.get_queryset())
        serializer = BlogReadSerializer(query, many=True)
        return Response(serializer.data, status=201)
