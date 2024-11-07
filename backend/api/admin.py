from django.contrib import admin

# Register your models here.
from .models import Line, LineStation, Station

admin.site.register(Station)
admin.site.register(Line)
admin.site.register(LineStation)

