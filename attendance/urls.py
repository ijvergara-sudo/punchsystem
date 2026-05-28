from django.urls import path
from .views import punch_view, reports_view

urlpatterns = [
    path('', punch_view),
    path('reports/', reports_view),
]
