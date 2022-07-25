from django.db import models

# Create your models here.

class pouser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    buyercookie = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    nombre_unico = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True)
    businessunit = models.CharField(max_length=100, null=True)
    urlToRedirect = models.CharField(max_length=100, null=True)
    secretID = models.CharField(max_length=100, null=True)
    sessionExpiredAt = models.DateTimeField(null=True)
    sessionOpen = models.BooleanField(null=True)
    concurrentSessions = models.IntegerField(null=True)
    totalSessions = models.IntegerField(null=True)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)