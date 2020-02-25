from django.db import models

class State(models.Model):
    Title = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    Id = models.AutoField(primary_key=True)
    Time = models.DateTimeField(auto_now_add=True)

