from django.contrib import admin
from .models import Employee, Punch

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "active")

@admin.register(Punch)
class PunchAdmin(admin.ModelAdmin):
    list_display = ("employee", "punch_type", "timestamp")
