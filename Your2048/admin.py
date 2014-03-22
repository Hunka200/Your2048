from django.contrib import admin
from .models import Game
import settings
import os

class GameAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name','url')
    search_fields = ['url']

admin.site.register(Game, GameAdmin)
