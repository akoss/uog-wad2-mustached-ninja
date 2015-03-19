from django.contrib import admin
from carwebsite.models import Manufacturer,Model

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Model,ModAdmin)