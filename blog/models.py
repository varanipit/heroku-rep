from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    feature_pic = models.ImageField(upload_to="cover/", null=True, blank=True)
    def __str__(self):
        return self.title