from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title