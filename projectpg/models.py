from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
class projects(models.Model):
    # idd=models.AutoField(primary_key=True,unique=True)
    heading=models.CharField(max_length=30,blank=False)
    img=CloudinaryField('image')
    # img=models.FileField(blank=True, null=True)
    description=models.CharField(max_length=180,blank=False)
    githublink=models.CharField()
    details=models.CharField(max_length=700)
    
    def __str__(self):
        return self.heading