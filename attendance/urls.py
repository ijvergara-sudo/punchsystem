from django.urls import path
from .views import punch_view, reports_view, live_punches_view

urlpatterns = [
    path('', punch_view),
    path('reports/', reports_view),
    path('live/', live_punches_view, name='live_punches'),
]


#from django.urls import path
#from .views import punch_view, reports_view

#urlpatterns = [
#    path('', punch_view),
#    path('reports/', reports_view),
#]
