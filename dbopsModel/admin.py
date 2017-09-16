from django.contrib import admin

# Register your models here.

from django.contrib import admin
from dbopsModel.models import dbuserinfo

class dbuserinfoadmin(admin.ModelAdmin):
    list_display = ('project_name','dbhost','dbname','user_name')
    search_fields = ('project_name','dbhost','dbname','user_name')
    # raw_id_fields = ('project_name','dbhost','dbname','user_name')

admin.site.register(dbuserinfo,dbuserinfoadmin)