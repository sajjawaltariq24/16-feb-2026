from django.db import models

class Organize(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Practice(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def _str_(self):
        return self.name