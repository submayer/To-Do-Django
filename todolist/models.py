from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=350)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
