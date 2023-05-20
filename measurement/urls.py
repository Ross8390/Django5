from django.urls import path

from .views import SensorView, ChangeSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', ChangeSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]