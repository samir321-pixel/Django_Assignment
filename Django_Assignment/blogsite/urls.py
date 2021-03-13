from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register('category', CategoryViewsets, 'category')
router.register('blog', BlogViewsets, 'blog')

urlpatterns = [
    path(r'', include(router.urls)),
]
