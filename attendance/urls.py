from django.urls import path
from .views import punch_view, reports_view, live_punches_view

urlpatterns = [
<<<<<<< HEAD
    path('', punch_view, name='punch'),
    path('reports/', reports_view, name='reports'),
    path('live/', live_punches_view, name='live_punches'),
]
=======
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
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
