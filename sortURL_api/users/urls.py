from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = router.urls