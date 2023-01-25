from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name