from django.db import models

# Create your models here.
class Kendaraan(models.Model):
    jenis = models.CharField(max_length=100, null=True)
    plat = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.plat
    
class Sensor(models.Model):
    suhu = models.FloatField(null=True)
    lokasi = models.CharField(max_length=100, null=True)
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"Suhu: {self.suhu}"