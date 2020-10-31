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

class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=False)    
    category_image=models.ImageField(null=True)

    def __str__(self):
        return self.category_name

    @property
    def imageURL(self):
        try:
            url = self.category_image.url
        except:
            url = ''

        return url


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=200, blank=False)    
    subcategory_photo=models.ImageField(null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.subcategory_name

    @property
    def imageURL(self):
        try:
            url = self.subcategory_photo.url
        except:
            url = ''

        return url