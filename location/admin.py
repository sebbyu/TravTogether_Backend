from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  list_display = ('place', 'slug', 'local_map',)
  list_filter = ('slug',)
  fieldsets = (
    (None, {'fields': ('place', 'local_map')}),
  )

  add_fieldsets = (
    (None, {'classes': ('wide',),
    'fields': ('place', 'local_map',)}),
  )



