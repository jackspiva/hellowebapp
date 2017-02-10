from django.contrib import admin

# import your models here.
from collection.models import Worksheet

# set up automated slug creation
class WorksheetAdmin(admin.ModelAdmin):
    model = Worksheet
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Worksheet, WorksheetAdmin)
