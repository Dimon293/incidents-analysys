from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from django.db import connection, models
from django.core import serializers

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import *
from .models import *
from .filters import *


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.filter().select_related('id_road').only(
        'id_road__title', 'street', 'house', 'latitude', 'longtitude')

    serializer_class = AddressSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ['street', 'id_road']
    ordering_fields = ['latitude', 'longtitude']


class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title']
    ordering_fields = ['title']


class DrivingChangeView(viewsets.ModelViewSet):
    queryset = Drivingchange.objects.all()
    serializer_class = DrivingChangeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class IncidentView(viewsets.ModelViewSet):
    queryset = Incident.objects.filter().select_related('id_address', 'id_address__id_road',
                                                        'id_address__id_road__id_locality',
                                                        'id_address__id_road__id_locality__id_district',
                                                        'id_type', 'id_roadwaystatus',
                                                        'id_lighting',
                                                        'id_drivingchange').only(
        'id_address__street', 'id_address__house', 'id_address__id_road', 'id_address__id_road__title',
        'id_address__id_road__id_locality',
        'id_type__value',
        'id_roadwaystatus__value', 'id_lighting__value',
        'id_drivingchange__value', 'date', 'time', 'deaths', 'wounds')

    serializer_class = IncidentSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filtering_fields = ['date']
    ordering_fields = ['date', 'time', 'deaths', 'wounds']


class IncidentTypeView(viewsets.ModelViewSet):
    queryset = Incidenttype.objects.all()
    serializer_class = IncidentTypeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class InfluenceFactorView(viewsets.ModelViewSet):
    queryset = Influencefactor.objects.all()
    serializer_class = InfluenceFactorSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class LightingView(viewsets.ModelViewSet):
    queryset = Lighting.objects.all()
    serializer_class = LightingSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class LocalityView(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class ObjectView(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class RoadDisadvantageView(viewsets.ModelViewSet):
    queryset = Roaddisadvantage.objects.all()
    serializer_class = RoadDisadvantageSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class RoadImportanceView(viewsets.ModelViewSet):
    queryset = Roadimportance.objects.all()
    serializer_class = RoadImportanceSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class RoadView(viewsets.ModelViewSet):
    queryset = Road.objects.filter().select_related('id_locality', 'id_importance',
                                                    'id_streetcategory').only(
        'id_locality__title', 'id_importance__value', 'id_streetcategory__value', 'title',
        'category')

    serializer_class = RoadSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['title', 'category']


class RoadwayStatusView(viewsets.ModelViewSet):
    queryset = Roadwaystatus.objects.all()
    serializer_class = RoadwayStatusSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class StreetCategoryView(viewsets.ModelViewSet):
    queryset = Streetcategory.objects.all()
    serializer_class = StreetCategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['title', 'id']


class WeatherView(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']
