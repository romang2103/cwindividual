"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import test, stations_api, station_api, lines_api, line_api, line_stations_api, line_station_api


urlpatterns = [
    path('test/', test, name='test'),
    path('stations/', stations_api, name='stations api'),
    path('station/<int:station_id>/', station_api, name='station api'),
    path('lines/', lines_api, name='lines api'),
    path('line/<int:line_id>/', line_api, name='line api'),
    path('line-stations/', line_stations_api, name='line stations api'),
    path('line-station/<int:line_station_id>/', line_station_api, name='line station api'),
]
