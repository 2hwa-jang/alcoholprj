from django.db import models
from django.utils import timezone
#from django.urls import reverse

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    #slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    #def get_absolute_url(self):
        #return reverse('alcohol:list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Post(models.Model):
    #STATUS_CHOICES = (
    #    ('draft', 'Draft'),
    #   ('published', 'Published'),
    #)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    title = models.CharField(max_length=250)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True)
    #slug = models.SlugField(max_length=250, unique=True)
    #seo_title = models.CharField(max_length=250)
    #seo_description = models.CharField(max_length=160)
    #status = models.CharField(max_length = 9, choices = STATUS_CHOICES)

    def __str__(self):
        return self.title