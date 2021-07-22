from django.db import models


# class Rate(models.Model):
#     sale = models.DecimalField(max_digits=5, decimal_places=2)
#     buy = models.DecimalField(max_digits=5, decimal_places=2)  # 32.45
#     created = models.DateTimeField(auto_now_add=True)
#     source = models.CharField(max_length=32)  # privatbank,monobank
#     type = models.CharField(max_length=3)  # USD, EUR


class ContactUs(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.IntegerField()
    mail = models.EmailField(max_length=100)

