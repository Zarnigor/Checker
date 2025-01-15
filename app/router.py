from rest_framework.routers import DefaultRouter

from app.views import SubmissionViewSet

router = DefaultRouter()
router.register(r'submissions', SubmissionViewSet)

router_urls = router.urls

