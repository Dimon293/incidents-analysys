from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'participantcategories', ParticipantCategoryView, basename='participantcategories')
router.register(r'participantactions', ParticipantActionView, basename='participantactions')
router.register(r'consiquences', ConsiquenceView, basename='consiquences')
router.register(r'violations', ViolationView, basename='violations')
router.register(r'participants', ParticipantView, basename='participants')

urlpatterns = router.urls
