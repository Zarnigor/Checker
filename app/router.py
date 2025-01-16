from rest_framework.routers import DefaultRouter

from app.views import SubmissionViewSet, ProblemListView

router = DefaultRouter()
router.register(r'submissions', SubmissionViewSet)
router.register(r'problems', ProblemListView)

router_urls = router.urls

