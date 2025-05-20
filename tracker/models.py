# tracker/models.py
from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interview', 'Interview'),
    ('rejected', 'Rejected'),
    ('offered', 'Offered'),
    ('accepted', 'Accepted'),
]

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True, null=True)
    application_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"

    class Meta:
        ordering = ['-application_date']