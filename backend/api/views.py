import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Station, Line

def test(request):
    return JsonResponse({
            'stations': [
                station.as_dict() for station in Station.objects.all()
            ],
            # 'lines': [
            #     line.as_dict() for line in Line.objects.all()
            # ]
        })


def stations_api(request):
    """API endpoint for the collection of stations"""
    
    if request.method == 'GET':
        return JsonResponse({
            'stations': [
                station.as_dict() for station in Station.objects.all()
            ]
        })

    elif request.method == 'POST':
        # Create a new station
        POST = json.loads(request.body)
        station = Station.objects.create(
            name=POST['name'],
        )
        return JsonResponse(station.as_dict())
    
    # Return a 405 Method Not Allowed response for all other request methods
    return HttpResponse(status=405)


def station_api(request, station_id):
    """API endpoint for a single computer"""
    station = Station.objects.get(id=station_id)
    print("Station to delete: ", station)

    if request.method == 'PUT':
        PUT = json.loads(request.body)
        station.name = PUT['name']
        station.save()
        return JsonResponse(station.as_dict())

    if request.method == 'DELETE':
        station.delete()
        return JsonResponse({})

    return JsonResponse(station.as_dict())


def lines_api(request):
    """API endpoint for the collection of lines"""
    if request.method == 'GET':
        return JsonResponse({
            'lines': [
                line.as_dict() for line in Line.objects.all()
            ]
        })
    elif request.method == 'POST':
        pass
    
    return HttpResponse(status=405)