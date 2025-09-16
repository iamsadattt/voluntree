from django.db import models
from django.conf import settings

class NGO(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ngo_profile')
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Event(models.Model):
    NGO_SKILL_LIMIT = 255
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    skills_required = models.CharField(max_length=NGO_SKILL_LIMIT, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.ngo.name}"

class VolunteerApplication(models.Model):
    STATUS = [('pending','Pending'),('approved','Approved'),('rejected','Rejected')]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event','volunteer')
