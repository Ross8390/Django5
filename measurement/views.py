from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        Sensor(name=name, description=description).save()
        return Response({'status': 'Готово'})


class ChangeSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        object = Sensor.objects.get(id=pk)
        if request.data.get('name'):
            object.name = request.data.get('name')
        if request.data.get('description'):
            object.description = request.data.get('description')
        object.save()
        return Response({'status': 'Готово'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor = Sensor.objects.get(id=request.data.get('sensor'))
        temperature = request.data.get('temperature')
        Measurement(sensor=sensor, temperature=temperature).save()
        return Response({'status': 'готово'})