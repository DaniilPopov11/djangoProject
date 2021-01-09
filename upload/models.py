from django.db import models


class Clients(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file

