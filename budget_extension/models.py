from django.db import models

# Create your models here.
class Extension(models.Model):
    Research_fellows = models.CharField(max_length=500)
    Extension_weeks = models.IntegerField()
    Project_completion = models.DateField()
    Reason_of_extension = models.TextField()
    Detail_remaining_work = models.TextField()
    Progress_report = models.FileField()

class Research_fellow(models.Model):
    Bud_utilize = models.IntegerField()
    Additional_bud = models.IntegerField()
    Justify = models.TextField()

class Material(models.Model):
    Bud_utilize = models.IntegerField()
    Additional_bud = models.IntegerField()
    Justify = models.TextField()

class Other(models.Model):
    Bud_utilize = models.IntegerField(blank=True)
    Additional_bud = models.IntegerField(blank=True)
    Justify = models.TextField(blank=True)