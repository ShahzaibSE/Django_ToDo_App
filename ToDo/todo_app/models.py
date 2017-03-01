from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

class Tasks(models.Model):
    # tid = models.BigIntegerField();
    task = models.CharField(max_length=200);

    def __str__(self):
        return self.task;