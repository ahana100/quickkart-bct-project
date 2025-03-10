from django.db import models

class user(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table="user"

# Create your models here.
