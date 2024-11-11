import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Station, Line, LineStation


def stations_api(request):
    """
    API endpoint for the collection of stations
    
    Supports GET and POST methods
    """
    
    if request.method == 'GET':
        # Retrieve and return all stations as JSON
        return JsonResponse({
            'stations': [
                station.as_dict() for station in Station.objects.all()
            ]
        })

    elif request.method == 'POST':
        # Create a new station item
        POST = json.loads(request.body)
        station = Station.objects.create(
            name=POST['name'],
        )
        return JsonResponse(station.as_dict())
    
    # Return a 405 Method Not Allowed response for all other request methods
    return HttpResponse(status=405)


def station_api(request, station_id):
    """
    API endpoint for handling operations on a single station
    
    Supports PUT, and DELETE methods
    """
    
    station = Station.objects.get(id=station_id)

    if request.method == 'PUT':
        # Update station attributes and save changes
        PUT = json.loads(request.body)
        station.name = PUT['name']
        station.save()
        return JsonResponse(station.as_dict())

    if request.method == 'DELETE':
        # Delete the station
        station.delete()
        return JsonResponse({})

    # Default response is the station data in JSON format
    return JsonResponse(station.as_dict())


def lines_api(request):
    """
    API endpoint for the collection of lines
    
    Supports GET and POST methods
    """
    
    if request.method == 'GET':
        # Retrieve and return all lines as JSON
        return JsonResponse({
            'lines': [
                line.as_dict() for line in Line.objects.all()
            ]
        })
        
    if request.method == 'POST':
        # Create a new line item
        POST = json.loads(request.body)
        line = Line.objects.create(
            name=POST['name'],
            number_of_stations=POST['numberOfStations'],
            available_on_weekend=POST['weekendAvailability']
        )
        return JsonResponse(line.as_dict())
    
    # Return a 405 Method Not Allowed response for all other request methods
    return HttpResponse(status=405)


def line_api(request, line_id):
    """
    API endpoint for handling operations on a single line
    
    Supports PUT, and DELETE methods
    """
    
    line = Line.objects.get(id=line_id)
    
    if request.method == 'PUT':
        # Update line attributes and save changes
        PUT = json.loads(request.body)
        line.name = PUT['name']
        line.number_of_stations = PUT['numberOfStations']
        line.available_on_weekend = PUT['weekendAvailability']
        line.save()
        return JsonResponse(line.as_dict())

    if request.method == 'DELETE':
        # Delete the line
        line.delete()
        return JsonResponse({})

    # Default response is the line data in JSON format
    return JsonResponse(line.as_dict())

def line_stations_api(request):
    """
    API endpoint for the collection of line-stations
    
    Supports GET and POST methods
    """
    
    if request.method == 'GET':
        return JsonResponse({
            'line-stations': [
                line_station.as_dict() for line_station in LineStation.objects.all()
            ]
        })
    
    if request.method == 'POST':
        # Create a new line-station item
        POST = json.loads(request.body)
        line = Line.objects.get(id=POST['line_id'])
        station = Station.objects.get(id=POST['station_id'])
        line_station = LineStation.objects.create(
            line=line,
            station=station,
            order=POST['order'],
            notes=POST['notes']
        )
        return JsonResponse(line_station.as_dict())
    
    # Return a 405 Method Not Allowed response for all other request methods
    return HttpResponse(status=405)

def line_station_api(request, line_station_id):
    """
    API endpoint for handling operations on a single line-station item
    
    Supports PUT, and DELETE methods
    """
    
    line_station = LineStation.objects.get(id=line_station_id)
    
    if request.method == 'PUT':
        PUT = json.loads(request.body)
        station = Station.objects.get(id=PUT['station']['id'])
        line = Line.objects.get(id=PUT['line']['id'])
        line_station.station = station
        line_station.line = line
        line_station.order = PUT['order']
        line_station.notes = PUT['notes']
        line_station.save()
        return JsonResponse(line_station.as_dict())
    
    if request.method == 'DELETE':
        line_station.delete()
        return JsonResponse({})

    return JsonResponse(line_station.as_dict())