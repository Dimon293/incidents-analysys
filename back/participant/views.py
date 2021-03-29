from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django.db import connection, models
from django.core import serializers
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import *
from .models import *


class ParticipantCategoryView(viewsets.ModelViewSet):
    queryset = Participantcategory.objects.all()
    serializer_class = ParticipantCategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class ParticipantActionView(viewsets.ModelViewSet):
    queryset = Participantaction.objects.all()
    serializer_class = ParticipantActionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class ConsiquenceView(viewsets.ModelViewSet):
    queryset = Consiquence.objects.all()
    serializer_class = ConsiquenceSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['value']


class ViolationView(viewsets.ModelViewSet):
    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['year']


class ParticipantView(viewsets.ModelViewSet):
    queryset = Participant.objects.all().select_related('id_incident', 'id_transport', 'id_category', 'id_action',
                                                        'id_consiquence').only(
        'id_incident__id', 'id_transport__id',
        'id_category__value', 'id_action__value',
        'id_consiquence__value', 'sex', 'isUsedSafetyBelt', 'drunkenness', 'drivingExperience')
    serializer_class = ParticipantSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    ordering_fields = ['sex', 'isUsedSafetyBelt', 'drunkenness']
