from django.contrib import admin
from .models import Horse
from .models import HorseOwner
from .models import Race
from .models import Expense

admin.site.register(Horse)
admin.site.register(HorseOwner)
admin.site.register(Race)
admin.site.register(Expense)
