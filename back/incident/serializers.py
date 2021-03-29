import json

from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    road = serializers.CharField(source='id_road')

    class Meta:
        model = Address
        fields = ('id', 'road', 'street', 'house', 'latitude', 'longtitude')


class DistrictSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='id_subject')

    class Meta:
        model = District
        fields = ('id', 'subject', 'title')


class DrivingChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivingchange
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        str = f'{{"id": "{data.id}", "value": "{data.value}"}}'
        json_str = json.loads(str)

        return json_str


class TinyIncidentSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(source='id_type', read_only=True)
    roadwayStatus = serializers.PrimaryKeyRelatedField(source='id_roadwaystatus', read_only=True)
    lighting = serializers.PrimaryKeyRelatedField(source='id_lighting', read_only=True)
    drivingChange = serializers.PrimaryKeyRelatedField(source='id_drivingchange', read_only=True)

    subject = serializers.CharField(source='id_address', read_only=True)


class IncidentSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='id_type', read_only=True)
    address = serializers.CharField(source='id_address', read_only=True)
    roadwayStatus = serializers.CharField(source='id_roadwaystatus', read_only=True)
    lighting = serializers.CharField(source='id_lighting', read_only=True)
    drivingChange = serializers.CharField(source='id_drivingchange', read_only=True)

    roadDisadvantages = serializers.StringRelatedField(many=True, read_only=True)
    weathers = serializers.StringRelatedField(many=True, read_only=True)
    influenceFactors = serializers.StringRelatedField(many=True, read_only=True)
    objectsOn = serializers.StringRelatedField(many=True, read_only=True)
    objectsNear = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Incident
        fields = ('id', 'date', 'time', 'address', 'type', 'lighting', 'roadwayStatus',
                  'drivingChange', 'deaths', 'wounds', 'influenceFactors', 'roadDisadvantages', 'weathers', 'objectsOn',
                  'objectsNear')


class IncidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidenttype
        fields = '__all__'


class InfluenceFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencefactor
        fields = '__all__'


class LightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lighting
        fields = '__all__'


class LocalitySerializer(serializers.ModelSerializer):
    district = serializers.CharField(source='id_district')

    class Meta:
        model = Locality
        fields = ('id', 'title', 'district')


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'


class RoadDisadvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roaddisadvantage
        fields = '__all__'


class RoadImportanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadimportance
        fields = '__all__'


class RoadSerializer(serializers.ModelSerializer):
    locality = serializers.CharField(source='id_locality')
    roadImportance = serializers.CharField(source='id_importance')
    streetCategory = serializers.CharField(source='id_streetcategory')

    class Meta:
        model = Road
        fields = ('id', 'locality', 'title', 'roadImportance', 'category', 'streetCategory')


class RoadwayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadwaystatus
        fields = '__all__'


class StreetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Streetcategory
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
