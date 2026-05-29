from django.db import models
from django.contrib.auth.hashers import make_password, check_password

<<<<<<< HEAD

=======
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
class Employee(models.Model):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    pin_hash = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now_add=True)

    def set_pin(self, raw_pin):
        self.pin_hash = make_password(str(raw_pin).strip())

    def check_pin(self, raw_pin):
        return check_password(str(raw_pin).strip(), self.pin_hash)

    def save(self, *args, **kwargs):
        if self.pin_hash and not self.pin_hash.startswith(("pbkdf2_", "argon2", "bcrypt")):
=======

    def set_pin(self, raw_pin):
        self.pin_hash = make_password(raw_pin)

    def check_pin(self, raw_pin):
        return check_password(raw_pin, self.pin_hash)

    def save(self, *args, **kwargs):
        if not self.pin_hash.startswith('pbkdf2_'):
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
            self.set_pin(self.pin_hash)
        super().save(*args, **kwargs)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.full_name} ({self.username})"


class Punch(models.Model):
    PUNCH_TYPES = [
        ("IN", "In"),
        ("OUT", "Out"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="punches")
    full_name = models.CharField(max_length=100)
    punch_type = models.CharField(max_length=3, choices=PUNCH_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.punch_type} - {self.timestamp}"
=======
        return self.full_name

class Punch(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    punch_type = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.punch_type}"
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
