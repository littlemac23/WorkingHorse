from django.contrib import admin
from . import models
# Register your models here.
class horseAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.horseData, horseAdmin)
