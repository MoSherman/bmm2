from django.contrib import admin

from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'tag_1', 'tag_2', 'tag_3', 'description')

admin.site.register(Room, RoomAdmin)
