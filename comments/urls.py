from rest_framework.routers import DefaultRouter

from comments.views import CommentsViewset

router = DefaultRouter()
router.register(r'', CommentsViewset, basename='comments')
urlpatterns = router.urls
