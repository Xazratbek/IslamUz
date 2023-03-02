from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=400)
    upload_date = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField()