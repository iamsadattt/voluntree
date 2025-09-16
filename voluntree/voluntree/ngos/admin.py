from django.contrib import admin
from .models import NGO, Event, VolunteerApplication

admin.site.register(NGO)
admin.site.register(Event)
admin.site.register(VolunteerApplication)
