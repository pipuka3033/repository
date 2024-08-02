from django.contrib import admin
from playlist.models import Bublik

@admin.register(Bublik)
class BublikAdmin(admin.ModelAdmin):
    pass
