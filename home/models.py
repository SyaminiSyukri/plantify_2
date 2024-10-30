from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='pic/%y/')

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    sname = models.CharField(max_length=150)
    tags = models.TextField()
    sdesc = models.TextField()
    ldesc = models.TextField()
    img = models.FileField(upload_to="pic/%y/")
    def __str__(self):
        return self.title
    class Meta:
        ordering=('id',)
    
    def get_absolute_url(self):
        return reverse('details',args=[self.id,self.slug])

class Notes(models.Model):
    plantname = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="pic/%y/")

    def __str__(self):
        return self.plantname
  
        
        

        