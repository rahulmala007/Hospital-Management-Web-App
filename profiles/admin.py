from django.contrib import admin
from .models import  *

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
# Register your models here.
admin.site.register(Patient,TaskAdmin)
admin.site.register(Doctor)
admin.site.register(Receptionist)
admin.site.register(HR)