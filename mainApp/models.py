from django.db import models

# Create your models here.

class ToDo(models.Model):
    Title = models.CharField(max_length = 100,blank = False)
    Description = models.TextField(blank = True)
    Date = models.DateField(blank = False)
    Completed = models.BooleanField(default=False)
    class Meta:
        app_label = 'mainApp'

    def __str__(self):
        return self.Title