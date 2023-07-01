from django.contrib import admin
from .models import *


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'phone_number', 'level')


admin.site.register(Member, MemberAdmin)
