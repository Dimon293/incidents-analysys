from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from .models import *


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['title']


class CarModelView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ['id', 'title']
    filter_fields = ['id_brand']
    ordering_fields = ['title']


class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ['value']
    ordering_fields = ['value']


class DriveTypeView(viewsets.ModelViewSet):
    queryset = Drivetype.objects.all()
    serializer_class = DriveTypeSerializer


class OwnershipTypeView(viewsets.ModelViewSet):
    queryset = Ownershiptype.objects.all()
    serializer_class = OwnershipTypeSerializer


class TechnicalIssueView(viewsets.ModelViewSet):
    queryset = Technicalissue.objects.all()
    serializer_class = TechnicalIssueSerializer


class TransportView(viewsets.ModelViewSet):
    queryset = Transport.objects.all().select_related('id_action', 'id_type', 'id_model', 'id_model__id_brand',
                                                      'id_color',
                                                      'id_drivetype',
                                                      'id_ownershiptype').only(
        'id_action__value', 'id_type__value',
        'id_model__title', 'id_model__id_brand',
        'id_color__value',
        'id_drivetype__value',
        'id_ownershiptype__value', 'year')
    serializer_class = TransportSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ['id_model', 'id']
    filter_fields = ['id_model']
    ordering_fields = ['year']


class TransportTechnicalIssueView(viewsets.ModelViewSet):
    queryset = TransportTechnicalissue.objects.all()
    serializer_class = TransportTechnicalIssueSerializer


class TransportActionView(viewsets.ModelViewSet):
    queryset = Transportaction.objects.all()
    serializer_class = TransportActionSerializer


class TransportTypeView(viewsets.ModelViewSet):
    queryset = Transporttype.objects.all()
    serializer_class = TransportTypeSerializer
