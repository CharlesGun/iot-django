from django.urls import path

from backend_app.api import masterdata

urlpatterns = [
    #MASTER KATEGORI
    path("sensor/post/<str:jenis_kendaraan>/<str:plat_kendaraan>", masterdata.postSensor, name="postSensor"),
    path("sensor/get/<str:jenis_kendaraan>/<str:plat_kendaraan>", masterdata.getSensorByKendaraan, name="getSensor"),
]