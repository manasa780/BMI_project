from django.db import models

class BMIRecord(models.Model):

    name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name