from rest_framework.routers import DefaultRouter
from newsletters.views import NewslettersViewSet

router = DefaultRouter()
router.register('newsletters', NewslettersViewSet)

urlpatterns = router.urls