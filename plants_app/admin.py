from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Plant)
admin.site.register(models.MedicinalPlant)
admin.site.register(models.PlantLocalName)
