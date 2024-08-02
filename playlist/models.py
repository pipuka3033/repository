from django.db import models

class Bublik(models.Model):
    title = models.CharField(max_length=55)
    embed = models.TextField()
    description = models.TextField(null=True, blank=True)