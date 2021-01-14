import datetime

from django.db import models

# Choices Sessions
CHOICES_SESSIONS = (
    ('Weekly Session', 'Weekly Session'),
    ('One Day Session', 'One Day Session'),
)
WEEKDAYS = (
  ("Monday", "Monday"),
  ("Tuesday", "Tuesday"),
  ("Wednesday", "Wednesday"),
  ("Thursday", "Thursday"),
  ("Friday", "Friday"),
  ("Saturday", "Saturday"),
  ("Sunday", "Sunday"),
)


# Data Doctor
class Doctor(models.Model):
    name = models.CharField(max_length=256)
    sessions = models.CharField(max_length=40, choices=CHOICES_SESSIONS)
    price = models.IntegerField(default=200)
    weekday = models.CharField(max_length=256,choices=WEEKDAYS,unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')


    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

    def __str__(self):
        return self.name


# Data Specialty
class Specialty(models.Model):
    name_sp = models.CharField(max_length=250, null=True, blank=True)
    sep = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return '%s ,Specialty: %s' % (self.sep, self.name_sp)


# Data Sessions
class Session(models.Model):
    name = models.CharField(max_length=50)
    title = models.ForeignKey(Specialty,on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.title)