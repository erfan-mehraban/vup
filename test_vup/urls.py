from rest_framework.routers import SimpleRouter

from .views import TestViewSet

router = SimpleRouter()
router.register(r'test', TestViewSet, base_name='test')
urlpatterns = router.urls
