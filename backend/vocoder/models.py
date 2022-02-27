from django.db import models

# Create your models here.

class Vocoder_audio_carrier(models.Model):
    record = models.FileField(upload_to='documents/')

    class Meta:
            db_table = 'Vocoder_audio_carrier'