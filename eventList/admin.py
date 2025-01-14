from django.contrib import admin
from .models import Event, TeamMember

# Register your models here.
admin.site.register(Event)
admin.site.register(TeamMember)