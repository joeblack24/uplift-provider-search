from django.contrib import admin
from .models import Provider
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider
class ProviderAdmin(ImportExportActionModelAdmin):
    resource_class = ProviderResource
    list_display = ('id', 'last_name', 'first_name')

admin.site.register(Provider, ProviderAdmin)