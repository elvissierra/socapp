from django.db import models


class Notifs(models.Model):
    # id = models.AutoField(primary_key = True)
    content = models.TextField()
    image = models.FileField(upload_to="images/", blank=True, null=True)
