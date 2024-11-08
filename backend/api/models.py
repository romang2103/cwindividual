from django.db import models
    
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
class Line(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    stations = models.ManyToManyField(Station, through="LineStation")
    number_of_stations = models.IntegerField()
    available_on_weekend = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'stations': [station.as_dict() for station in self.stations.all()],
            'number_of_stations': self.number_of_stations,
            'available_on_weekend': self.available_on_weekend,
            'date_created': self.date_created
        }

class LineStation(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    
    
    def __str__(self):
        return f"{self.line} - {self.station} - {self.order}"