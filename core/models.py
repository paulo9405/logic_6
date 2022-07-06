from django.db import models
from datetime import datetime

class Double(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    double_value = models.IntegerField(blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.double_value = self.value * 2
        return super(Double, self).save(*args, **kwargs)
