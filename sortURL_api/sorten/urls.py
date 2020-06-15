from rest_framework.routers import SimpleRouter
from .views import SortenViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'create', SortenViewSet)

urlpatterns = router.urls