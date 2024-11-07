from django.db import models
    
class Station(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
class Line(models.Model):
    name = models.CharField(max_length=128)
    stations = models.ManyToManyField(Station, through="LineStation")
    number_of_stations = models.IntegerField()
    available_on_weekend = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class LineStation(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    
    
    def __str__(self):
        return f"{self.line} - {self.station} - {self.order}"