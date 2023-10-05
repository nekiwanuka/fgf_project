from django.contrib import admin
from .models import (
    Region,
    LifeForm,
    Value,
    ValueDetail,
    OtherValueDetail,
    Plant,
    PlantLocalName,
    MedicinalPlant
)

admin.site.register(Region)
admin.site.register(LifeForm)
admin.site.register(Value)
admin.site.register(ValueDetail)
admin.site.register(OtherValueDetail)
admin.site.register(Plant)
admin.site.register(PlantLocalName)
admin.site.register(MedicinalPlant)
