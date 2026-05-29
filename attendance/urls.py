from django.urls import path
from .views import punch_view, reports_view, live_punches_view

urlpatterns = [
    path('', punch_view, name='punch'),
    path('reports/', reports_view, name='reports'),
    path('live/', live_punches_view, name='live_punches'),
]
