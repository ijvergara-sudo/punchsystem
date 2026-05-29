<<<<<<< HEAD
from django import forms
from django.contrib import admin
from .models import Employee, Punch


class EmployeeAdminForm(forms.ModelForm):
    pin = forms.CharField(
        label="PIN",
        required=False,
        widget=forms.PasswordInput(render_value=True),
        help_text="Enter a new PIN to set or change it. Leave blank to keep the current PIN."
    )

    class Meta:
        model = Employee
        fields = ("username", "full_name", "pin", "active")

    def save(self, commit=True):
        employee = super().save(commit=False)

        pin = self.cleaned_data.get("pin")
        if pin:
            employee.set_pin(pin)

        if commit:
            employee.save()

        return employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = ("username", "full_name", "active", "created_at")
    search_fields = ("username", "full_name")
    list_filter = ("active",)


@admin.register(Punch)
class PunchAdmin(admin.ModelAdmin):
    list_display = ("employee", "full_name", "punch_type", "timestamp")
    search_fields = ("employee__username", "full_name")
    list_filter = ("punch_type", "timestamp")
    ordering = ("-timestamp",)
=======
from django.contrib import admin
from .models import Employee, Punch

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "active")

@admin.register(Punch)
class PunchAdmin(admin.ModelAdmin):
    list_display = ("employee", "punch_type", "timestamp")
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
