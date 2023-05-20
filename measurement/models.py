from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', null=False)
    description = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',
                               verbose_name='Модель датчика')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    image_model = models.ImageField(upload_to='images/', null=True, blank=True, max_length=255)