from django.contrib import admin

# Register your models here.

from django.contrib import admin
from dbopsModel.models import dbuserinfo,dbinfo

class dbuserinfoadmin(admin.ModelAdmin):
    list_display = ('project_name','dbhost','dbname','user_name')
    search_fields = ('project_name','dbhost','dbname','user_name')
    # raw_id_fields = ('project_name','dbhost','dbname','user_name')
class dbinfoadmin(admin.ModelAdmin):
    list_display = ('t_project_name','t_dbhost','t_rootpasswd')
    search_fields = ('t_project_name','t_dbhost','t_rootpasswd')

admin.site.register(dbuserinfo,dbuserinfoadmin)
admin.site.register(dbinfo,dbinfoadmin)