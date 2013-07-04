from django.contrib import admin
from .models import ManualPage

class ManualPageAdmin(admin.ModelAdmin):
    class Meta:
        model = ManualPage

admin.site.register(ManualPage, ManualPageAdmin)
