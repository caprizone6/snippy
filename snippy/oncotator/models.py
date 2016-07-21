from django.db import models
from django.conf import settings
from django.utils.timezone import activate

activate(settings.TIME_ZONE)

class CSVFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    result = models.FileField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default =1)
    upload_time = models.DateTimeField(auto_now=True, auto_now_add=False)

