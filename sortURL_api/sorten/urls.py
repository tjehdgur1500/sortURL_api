from rest_framework.routers import SimpleRouter
from .views import SortenViewSet, RetriveViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'create', SortenViewSet)
router.register(r'cuturl', RetriveViewSet)

urlpatterns = router.urls
