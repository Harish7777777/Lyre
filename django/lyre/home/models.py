from django.db import models

class Lyre(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    song = models.FileField(upload_to='lyre_songs/', null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
