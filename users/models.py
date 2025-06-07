from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=128, validators=[MinLengthValidator(6)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    age = models.IntegerField(editable=False)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        from datetime import date
        today = date.today()
        age = today.year - self.dob.year
        if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
            age -= 1
        self.age = age
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username