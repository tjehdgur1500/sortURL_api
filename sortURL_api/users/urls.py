from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'signup', UserViewSet)

urlpatterns = router.urls