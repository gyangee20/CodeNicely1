from django.db import models

from django.db import models
class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.IntegerField(primary_key=True, default=10)
    dob = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10)


class UpdateOTP(models.Model):
    otp_mobile = models.IntegerField(primary_key=True,default=10)
    otp = models.CharField(max_length=10)



