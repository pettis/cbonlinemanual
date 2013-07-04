from django.contrib import admin
from .models import ManualPage


class ManualPageAdmin(admin.ModelAdmin):
    class Meta:
        model = ManualPage
        prepopulated_fields = {'slug': ('title',), }


admin.site.register(ManualPage, ManualPageAdmin)
