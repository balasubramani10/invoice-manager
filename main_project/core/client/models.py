from django.db import models

class Client(models.Model):
    LOCATION_CHOICES = [
        ('local', 'Local'),
        ('international', 'International'),
    ]

    TYPE_CHOICES = [
        ('first', 'First'),
        ('second', 'Second'),
        ('third', 'Third'),
    ]

    account_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=64)
    local_address = models.TextField(max_length=512, blank=True)
    permanent_address = models.TextField(max_length=512, blank=True)

    tel = models.CharField(max_length=15, blank=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    gst = models.CharField("GST Number", max_length=15, blank=True)
    location = models.CharField(max_length=13, choices=LOCATION_CHOICES, default='local')
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='first')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.account_no})"
