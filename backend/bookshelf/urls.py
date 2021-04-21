from django.urls import path

from rest_framework import routers

from .views import BooksViewSet

router = routers.DefaultRouter()
router.register('books', BooksViewSet)

urlpatterns = router.urls