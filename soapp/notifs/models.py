from django.db import models


class Notifs(models.Model):
    # id = models.AutoField(primary_key = True)
    content = models.TextField()
