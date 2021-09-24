from django.contrib import admin
from currency.models import Rate, Source, ContactUs
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin

from currency.resources import RateResource


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'source',
        'currency_type',
        'created',

    )
    list_filter = (
        'source',
        'currency_type',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'source',
        'type',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
    )

    list_filter = (
        'name',
        'source_url',
    )

    readonly_fields = (
        'id',
        'name',
        'source_url',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Source, SourceAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'firstname',
        'lastname',
        'mail',
        'body',
    )
    list_filter = (
        'mail',
    )

    readonly_fields = (
        'firstname',
        'lastname',
        'mail',
        'body',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
