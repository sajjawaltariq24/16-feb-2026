from django.db import models
from core.models import Patient

class Claim(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)

    def _str_(self):
        return {self.id}


class Payment(models.Model):
    claim = models.ForeignKey(Claim,on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8,decimal_places=2)
