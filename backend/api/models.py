from django.db import models
    
# Model representing a station
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        """Return the station name as the string representation."""
        return self.name
    
    def as_dict(self):
        """Return the station data as a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }
    
# Model representing a line
class Line(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    stations = models.ManyToManyField(Station, through="LineStation")
    number_of_stations = models.IntegerField()
    available_on_weekend = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the line name as the string representation."""
        return self.name
    
    def as_dict(self):
        """Return the line data as a dictionary, including nested station data."""
        return {    
            'id': self.id,
            'name': self.name,
            'stations': [station.as_dict() for station in self.stations.all()],
            'numberOfStations': self.number_of_stations,
            'weekendAvailability': self.available_on_weekend,
            'dateCreated': self.date_created
        }

# Through model for the relationship between Line and Station
class LineStation(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    
    
    def __str__(self):
        """Return a string representation showing the line, station, and order."""
        return f"{self.line} - {self.station} - {self.order}"
    
    def as_dict(self):
        """Return the line-station data as a dictionary, including nested station and line data."""
        return {
            'id': self.id,  
            'station': self.station.as_dict(),
            'line': self.line.as_dict(),
            'order': self.order,
            'notes': self.notes
        }