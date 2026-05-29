from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.admin.views.decorators import staff_member_required
from .models import Employee, Punch
=======
from .models import Employee, Punch
from django.contrib.admin.views.decorators import staff_member_required
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7


def punch_view(request):
    message = ""
<<<<<<< HEAD
    message_type = ""
    employee_name = ""
    employee_punches = []

    if request.method == "POST":
        full_name_input = request.POST.get("full_name", "").strip()
        username = request.POST.get("username", "").strip()
        pin = request.POST.get("pin", "").strip()
=======
    employee_punches = []
    employee_name = ""

    if request.method == "POST":
        username = request.POST.get("username")
        pin = request.POST.get("pin")
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7

        employee = Employee.objects.filter(
            username__iexact=username,
            active=True
        ).first()

        if employee and employee.check_pin(pin):
            last_punch = Punch.objects.filter(
                employee=employee
            ).order_by("-timestamp").first()

            punch_type = "OUT" if last_punch and last_punch.punch_type == "IN" else "IN"

<<<<<<< HEAD
            # Store name on punch. If user typed a name, store that;
            # otherwise store the employee profile name.
            punch_full_name = full_name_input or employee.full_name

            Punch.objects.create(
                employee=employee,
                full_name=punch_full_name,
                punch_type=punch_type
            )

            message = f"{punch_full_name} punched {punch_type} successfully."
            message_type = "success"
            employee_name = punch_full_name
=======
            Punch.objects.create(
                employee=employee,
                punch_type=punch_type
            )

            message = f"{employee.full_name} punched {punch_type}"
            employee_name = employee.full_name
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7

            employee_punches = Punch.objects.filter(
                employee=employee
            ).order_by("-timestamp")[:10]
        else:
<<<<<<< HEAD
            message = "Invalid username or PIN."
            message_type = "error"

    return render(request, "attendance/punch.html", {
        "message": message,
        "message_type": message_type,
=======
            message = "Invalid username or PIN"

    return render(request, "attendance/punch.html", {
        "message": message,
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
        "employee_name": employee_name,
        "employee_punches": employee_punches,
    })


def reports_view(request):
<<<<<<< HEAD
    punches = Punch.objects.select_related("employee").order_by("-timestamp")
    return render(request, "attendance/reports.html", {
        "punches": punches,
    })


=======
    punches = Punch.objects.all().order_by("-timestamp")
    return render(request, "attendance/reports.html", {"punches": punches})
    
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
@staff_member_required
def live_punches_view(request):
    punches = Punch.objects.select_related("employee").order_by("-timestamp")[:50]

<<<<<<< HEAD
    latest_by_employee = {}
    for punch in Punch.objects.select_related("employee").order_by("employee_id", "-timestamp"):
        if punch.employee_id not in latest_by_employee:
            latest_by_employee[punch.employee_id] = punch

    employees_in = [
        punch for punch in latest_by_employee.values()
=======
    currently_in = {}

    for punch in Punch.objects.select_related("employee").order_by("employee_id", "-timestamp"):
        if punch.employee_id not in currently_in:
            currently_in[punch.employee_id] = punch

    employees_in = [
        punch for punch in currently_in.values()
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
        if punch.punch_type == "IN"
    ]

    return render(request, "attendance/live_punches.html", {
        "punches": punches,
        "employees_in": employees_in,
<<<<<<< HEAD
    })
=======
    })
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
