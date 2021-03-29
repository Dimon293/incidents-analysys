import json

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='id_brand')

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'title')


class CarModelNewSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        brand = self.fields['id_brand']
        brand_title = brand.to_representation(
            brand.get_attribute(data)
        )

        str = '{"id": "%s", "title": "%s", "id_brand": "%s"}' % (data.id, data.title, brand_title)
        json_str = json.loads(str)

        return json_str

    class Meta:
        model = CarModel
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivetype
        fields = '__all__'


class OwnershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownershiptype
        fields = '__all__'


class TechnicalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technicalissue
        fields = '__all__'


class TransportTechnicalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTechnicalissue
        fields = '__all__'


class TransportActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportaction
        fields = '__all__'


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporttype
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):

    def to_representation(self, data):
        str = f'{{"id": "{data.id}", "value": "{data.value}"}}'
        json_str = json.loads(str)

        return json_str


class TransportSerializer(serializers.ModelSerializer):
    action = serializers.CharField(read_only=True, source='id_action')
    type = serializers.CharField(read_only=True, source='id_type')
    model = serializers.CharField(read_only=True, source='id_model')
    brand = serializers.SerializerMethodField()
    color = serializers.CharField(read_only=True, source='id_color')
    driveType = serializers.CharField(read_only=True, source='id_drivetype')
    ownershipType = serializers.CharField(source='id_ownershiptype')

    technicalissues = serializers.StringRelatedField(many=True, read_only=True)

    def get_brand(self, obj):
        return obj.id_model.id_brand.title

    class Meta:
        model = Transport
        fields = (
        'id', 'action', 'type', 'brand', 'model', 'color', 'driveType', 'year', 'ownershipType', 'technicalissues')
