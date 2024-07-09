from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model): 
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    text= models.CharField(max_length=1000)
    created_at= models.DateTimeField(default=timezone.now)
    published_at= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_at= timezone.now()
        self.save()

    def __str__(self):
        return self.title

