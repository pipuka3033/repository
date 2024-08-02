from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    images = models.ImageField(upload_to="Blop/images")
    likes = models.PositiveIntegerField(default=0)
    drafts = models.BooleanField(default=False)
    is_published = models.DateTimeField(auto_now_add=True)
