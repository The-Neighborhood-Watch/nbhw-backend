from django.db import models


class StatusTypes(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class Entity(models.Model):

    UK = "UNKNOWN"
    M = "MALE"
    F = "FEMALE"
    O = "OTHER"

    GENDER_CHOICES = (
        (UK, "Unknown"),
        (M, "Male"),
        (F, "Female"),
        (O, "Other")
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=UK)
    description = models.TextField()
    account_status = models.CharField(max_length=8, choices=StatusTypes.choices, default=StatusTypes.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
