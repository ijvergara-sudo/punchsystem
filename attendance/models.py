from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Employee(models.Model):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    pin_hash = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def set_pin(self, raw_pin):
        self.pin_hash = make_password(str(raw_pin).strip())

    def check_pin(self, raw_pin):
        return check_password(str(raw_pin).strip(), self.pin_hash)

    def save(self, *args, **kwargs):
        if self.pin_hash and not self.pin_hash.startswith(("pbkdf2_", "argon2", "bcrypt")):
            self.set_pin(self.pin_hash)
        super().save(*args, **kwargs)

    def __str__(self):

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

