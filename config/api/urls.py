from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = router.urls