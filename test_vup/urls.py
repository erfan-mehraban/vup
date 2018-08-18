from .views import TestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'test', TestViewSet, base_name='test')
urlpatterns = router.urls