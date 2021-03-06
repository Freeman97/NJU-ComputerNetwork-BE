from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('router/<str:router>', views.routeTable, name='routeTable'),
    path('router/<str:router>/interfaces', views.get_interfaces, name='get_interfaces'),
    path('router/<str:router>/noroutecache', views.disable_route_cache, name='disable_route_cache'),
    path('router/<str:router>/<str:intType>/<str:intId>', views.set_interface, name='set_interface'),
    path('router/<str:router>/ippacket', views.send_packet, name='send_packet'),
]
