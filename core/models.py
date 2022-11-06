from django.db import models

POSITION_CHOICES = (
    ('member','member'),
    ('developrer', 'developer'),
    ('instructor', 'instructor')
)
# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    email = models.CharField(max_length = 200, unique = True)
    bio = models.TextField(blank = True, null = True)
    position = models.CharField(max_length = 50, choices = POSITION_CHOICES)
    is_active = models.BooleanField(default = True)

class Contact(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    # message = models.TextField(blank = True, null = True)
