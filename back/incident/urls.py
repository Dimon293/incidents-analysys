from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'addresses', AddressView, basename='addresses')
router.register(r'drivingchanges', DrivingChangeView, basename='drivingchanges')
router.register(r'districts', DistrictView, basename='districts')
router.register(r'incidents', IncidentView, basename='incidents')
router.register(r'incidenttypes', IncidentTypeView, basename='incidenttypes')
router.register(r'influencefactors', InfluenceFactorView, basename='influencefactors')
router.register(r'lightings', LightingView, basename='lightnings')
router.register(r'localities', LocalityView, basename='localities')
router.register(r'objects', ObjectView, basename='objects')
router.register(r'roaddisadvantages', RoadDisadvantageView, basename='roaddisadvantages')
router.register(r'roadimportances', RoadImportanceView, basename='roadimportances')
router.register(r'roads', RoadView, basename='roads')
router.register(r'roadwaystatuses', RoadwayStatusView, basename='roadwaystatuses')
router.register(r'streetcategories', StreetCategoryView, basename='streetcategories')
router.register(r'subjects', SubjectView, basename='subjects')
router.register(r'weathers', WeatherView, basename='weathers')
urlpatterns = router.urls
