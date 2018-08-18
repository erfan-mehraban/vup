from rest_framework.routers import SimpleRouter

from .views import TestViewSet, TestViewSet2

router = SimpleRouter()
router.register(r'test', TestViewSet, base_name='test')
urlpatterns = router.urls
