from rest_framework.routers import DefaultRouter
from tags.views import TagsViewSet

router = DefaultRouter()
router.register('tags', TagsViewSet)

urlpatterns = router.urls