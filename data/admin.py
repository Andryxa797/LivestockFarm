from django.contrib import admin

from data.models import DataBeforeProcess, DataAfterProcess


class DataBeforeProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'DataTimeCreate', 'NewPost')
    list_filter = ('id', 'user', 'DataTimeCreate', 'NewPost')


class DataAfterProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'HeartBeat', 'CowCondition')
    list_filter = ('id', 'user', 'HeartBeat', 'CowCondition')


admin.site.register(DataBeforeProcess, DataBeforeProcessAdmin)
admin.site.register(DataAfterProcess, DataAfterProcessAdmin)
