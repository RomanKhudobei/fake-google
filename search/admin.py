from django.contrib import admin

from search.models import RandomText, ShowLog


class RandomTextModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'enabled')
    list_filter = ('enabled',)
    search_fields = ('text',)

    def enable(self, request, queryset):
        queryset.update(enabled=True)

    def disable(self, request, queryset):
        queryset.update(enabled=False)

    enable.short_description = 'Enable'
    disable.short_description = 'Disable'
    actions = (enable, disable)


class ShowLogModelAdmin(admin.ModelAdmin):
    list_display = ('shown', 'created_at')
    search_fields = ('shown__text',)


admin.site.register(RandomText, RandomTextModelAdmin)
admin.site.register(ShowLog, ShowLogModelAdmin)
