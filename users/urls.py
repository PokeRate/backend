from rest_framework.routers import DefaultRouter

from .views import UserViewset

router = DefaultRouter()
router.register(r'', UserViewset, basename='user')
urlpatterns = router.urls
