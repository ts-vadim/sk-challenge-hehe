from django.contrib import admin

# Register your models here.
from .models import KrakenRecord
from .models import SiteMember

admin.site.register(KrakenRecord)
admin.site.register(SiteMember)