from rest_framework.routers import DefaultRouter

from .views import BrandView, CarModelView, ColorView, DriveTypeView, OwnershipTypeView, TechnicalIssueView, \
    TransportActionView, TransportTypeView, TransportView, TransportTechnicalIssueView

router = DefaultRouter()
router.register(r'brands', BrandView, basename='brands')
router.register(r'models', CarModelView, basename='models')
router.register(r'colors', ColorView, basename='colors')
router.register(r'drivetypes', DriveTypeView, basename='drivetypes')
router.register(r'ownershiptypes', OwnershipTypeView, basename='ownershiptypes')
router.register(r'technicalissues', TechnicalIssueView, basename='technicalissues')
router.register(r'transports', TransportView, basename='transports')
router.register(r'transportactions', TransportActionView, basename='transportactions')
router.register(r'transporttypes', TransportTypeView, basename='transporttypes')
router.register(r'transporttechnicalissues', TransportTechnicalIssueView, basename='transporttechnicalissues')
urlpatterns = router.urls
