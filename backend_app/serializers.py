from rest_framework import serializers
from .models import *

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id","suhu", "lokasi", "created_at"]
        depth = 1

class KendaraanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kendaraan
        fields = "__all__"
        depth = 1