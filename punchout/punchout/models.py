from django.db import models

# Create your models here.

class pouser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default='probas')
    buyercookie = models.CharField(max_length=100, default='probas')
    apellido = models.CharField(max_length=100, default='probas')
    nombre_unico = models.CharField(max_length=100, default='probas')
    email = models.CharField(max_length=100, default='probas')
    user = models.CharField(max_length=100, default='probas')
    businessunit = models.CharField(max_length=100, default='probas')
    urlToRedirect = models.CharField(max_length=100, default='probas')
    secretID = models.CharField(max_length=100, default='probas')
    sessionExpiredAt = models.DateTimeField(null=True)
    sessionOpen = models.BooleanField(null=True)
    concurrentSessions = models.IntegerField(null=True)
    totalSessions = models.IntegerField(null=True)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)