from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend_app.models import *
from backend_app.serializers import *

@api_view(["POST"])
def postSensor(request, plat_kendaraan, jenis_kendaraan):
    data = request.data
    kendaraan, created = Kendaraan.objects.get_or_create(
        plat = plat_kendaraan,
        jenis = jenis_kendaraan
        )
    if created:
        kendaraan.save()
    sensor = Sensor.objects.create(
        suhu = data["suhu"],
        lokasi = data["lokasi"],
        kendaraan_id = kendaraan.pk
        )
    sensor.save()

    sensor_serializer = SensorSerializer(sensor)
    kendaraan_serializer = KendaraanSerializer(kendaraan)
    return Response({"status": 200, "messages": "Data Berhasil Ditambah!", "data": {"sensor":sensor_serializer.data, "kendaraan":kendaraan_serializer.data}})

@api_view(["GET"])
def getSensorByKendaraan(request, plat_kendaraan, jenis_kendaraan):
    kendaraan = Kendaraan.objects.get(
        plat = plat_kendaraan,
        jenis = jenis_kendaraan
        )
    sensor = Sensor.objects.filter(
        kendaraan_id = kendaraan.pk
        )

    sensor_serializer = SensorSerializer(sensor, many=True)
    kendaraan_serializer = KendaraanSerializer(kendaraan)
    return Response({"status": 200, "messages": "Data Berhasil Ditambah!", "data": { "kendaraan":kendaraan_serializer.data, "sensor":sensor_serializer.data}})