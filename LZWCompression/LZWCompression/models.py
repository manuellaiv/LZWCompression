from django.db import models

# Create your models here.
class Translation(models.Model):
    inp = models.CharField(max_length=200)
    out = models.CharField(max_length=200)
    status = models.IntegerField()

    def __str__(self):
        return str(self.status)

    class Meta:
        app_label = 'LZWCompression'