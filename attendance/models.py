from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Employee(models.Model):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    pin_hash = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def set_pin(self, raw_pin):
        self.pin_hash = make_password(raw_pin)

    def check_pin(self, raw_pin):
        return check_password(raw_pin, self.pin_hash)

    def save(self, *args, **kwargs):
        if not self.pin_hash.startswith('pbkdf2_'):
            self.set_pin(self.pin_hash)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Punch(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    punch_type = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.punch_type}"
