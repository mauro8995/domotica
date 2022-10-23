from django.urls import path
from home_domotica import views
urlpatterns = [
    path('', views.index, name="index"),
    path('focos_cambios', views.prender_foco)
]