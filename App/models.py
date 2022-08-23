from django.db import models

# Create your models here.


class Event(models.Model):
    academicyear = models.CharField(max_length=100)
    eventname = models.TextField()
    eventfocus = models.TextField()
    eventstartdate = models.DateField()
    eventenddate = models.DateField()
    eventvenue = models.TextField()
    eventresourceperson = models.TextField()
    starttime = models.TextField()
    endtime = models.TextField()

    def __str__(self):
        return self.eventname
