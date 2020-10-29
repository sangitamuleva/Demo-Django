from django.db import models
from django.urls import reverse

# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()    
    status = models.IntegerField(choices=STATUS, default=0)
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse ('all_post')

