import json

from rest_framework import serializers

from .models import *


class ParticipantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantcategory
        fields = '__all__'


class ConsiquenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consiquence
        fields = '__all__'


class ParticipantActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantaction
        fields = '__all__'


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'


class ParticipantViolationAssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantViolationAssociate
        fields = '__all__'


class ParticipantViolationImmediateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantViolationImmediate
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        str = '{"id": "%s", "value": "%s"}' % (data.id, data.value)
        json_str = json.loads(str)

        return json_str


class ParticipantSerializer(serializers.ModelSerializer):
    incident = serializers.CharField(source='id_incident')
    transport = serializers.CharField(source='id_transport')
    category = serializers.CharField(read_only=True, source='id_category')
    action = serializers.CharField(read_only=True, source='id_action')
    consiquence = serializers.CharField(read_only=True, source='id_consiquence')
    isUsedSafetyBelt = serializers.BooleanField()
    drivingExperience = serializers.IntegerField()

    violationsAssociate = serializers.StringRelatedField(many=True, read_only=True)
    violationsImmediate = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Participant
        fields = (
        'id', 'incident', 'transport', 'category', 'action', 'sex', 'consiquence', 'isUsedSafetyBelt', 'drunkenness',
        'drivingExperience', 'violationsAssociate', 'violationsImmediate')
