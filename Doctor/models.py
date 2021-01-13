import datetime

from django.db import models

# Choices Sessions
CHOICES_SESSIONS = (
    ('Weekly Session', 'Weekly Session'),
    ('One Day Session', 'One Day Session'),
)



# Data Doctor


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    sessions = models.CharField(max_length=40, choices=CHOICES_SESSIONS)
    price = models.IntegerField(null=True, blank=True, default=200)
    working_hours = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.name


# Data Specialty
class Specialty(models.Model):
    name_sp = models.CharField(max_length=250, null=True, blank=True)
    sep = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True, blank=True,)

    def __str__(self):
        return self.name_sp


# Data Sessions
class Session(models.Model):
    name = models.CharField(max_length=50)
    title = models.ForeignKey(Specialty,on_delete=models.CASCADE)
    price = models.IntegerField(default=200)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.title)