from django.shortcuts import render
from .models import Employee, Punch
from django.contrib.admin.views.decorators import staff_member_required


def punch_view(request):
    message = ""
    employee_punches = []
    employee_name = ""

    if request.method == "POST":
        username = request.POST.get("username")
        pin = request.POST.get("pin")

        employee = Employee.objects.filter(
            username__iexact=username,
            active=True
        ).first()

        if employee and employee.check_pin(pin):
            last_punch = Punch.objects.filter(
                employee=employee
            ).order_by("-timestamp").first()

            punch_type = "OUT" if last_punch and last_punch.punch_type == "IN" else "IN"

            Punch.objects.create(
                employee=employee,
                punch_type=punch_type
            )

            message = f"{employee.full_name} punched {punch_type}"
            employee_name = employee.full_name

            employee_punches = Punch.objects.filter(
                employee=employee
            ).order_by("-timestamp")[:10]
        else:
            message = "Invalid username or PIN"

    return render(request, "attendance/punch.html", {
        "message": message,
        "employee_name": employee_name,
        "employee_punches": employee_punches,
    })


def reports_view(request):
    punches = Punch.objects.all().order_by("-timestamp")
    return render(request, "attendance/reports.html", {"punches": punches})
    
@staff_member_required
def live_punches_view(request):
    punches = Punch.objects.select_related("employee").order_by("-timestamp")[:50]

    currently_in = {}

    for punch in Punch.objects.select_related("employee").order_by("employee_id", "-timestamp"):
        if punch.employee_id not in currently_in:
            currently_in[punch.employee_id] = punch

    employees_in = [
        punch for punch in currently_in.values()
        if punch.punch_type == "IN"
    ]

    return render(request, "attendance/live_punches.html", {
        "punches": punches,
        "employees_in": employees_in,
    })