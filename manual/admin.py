from django.contrib import admin
from .models import ManualPage


class ManualPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

    class Meta:
        model = ManualPage


admin.site.register(ManualPage, ManualPageAdmin)
