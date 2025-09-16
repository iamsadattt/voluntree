from django.db import models
from django.conf import settings

class VolunteerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vol_profile')
    skills = models.TextField(blank=True)
    total_hours = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Certificate(models.Model):
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=255)
    issued_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} for {self.volunteer.username}"
