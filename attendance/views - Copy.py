from django.shortcuts import render
from .models import Employee, Punch

def punch_view(request):
    message = ""

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
        else:
            message = "Invalid username or PIN"

    return render(request, "attendance/punch.html", {
        "message": message
    })

def reports_view(request):
    punches = Punch.objects.all().order_by("-timestamp")

    return render(request, "attendance/reports.html", {
        "punches": punches
    })
