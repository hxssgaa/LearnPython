from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    # Inner class Meta sets the default ordering attribute
    class Meta:
        ordering = ('-timestamp',)
