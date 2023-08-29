from django.contrib import admin
from .models import Employee


#Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['char_field', 'text_field', 'integer_field', 'float_field', 'ip_address', 'date_field',
                    'datetime_field', 'decimal_field', 'email_field', 'file_field']


admin.site.register(Employee, ProfileAdmin)
