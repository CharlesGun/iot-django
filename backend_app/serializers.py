from rest_framework import serializers
from .models import *

class Sensor(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id","value"]
        depth = 1