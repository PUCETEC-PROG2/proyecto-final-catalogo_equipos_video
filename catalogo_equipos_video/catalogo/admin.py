from django.contrib import admin
from .models import DVD, VHS, VideoEquipments

# Register your models here.
@admin.register(DVD)
class DVDAdmin(admin.ModelAdmin):
    pass
@admin.register(VHS)
class VHSAdmin(admin.ModelAdmin):
    pass
@admin.register(VideoEquipments)
class VEAdmin(admin.ModelAdmin):
    pass