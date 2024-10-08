from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=50, choices=[
        ('web_app', 'Web App'),
        ('full_stack_app', 'Full Stack App'),
        ('android_app', 'Android App'),
        ('ios_app', 'Ios App'),
        ('rest_api', 'REST API'),
        ('web_backend', 'Web Backend'),
        ('core_python', 'Core Python'),
        ('other', 'Other')
    ])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=False,editable=False)
    def __str__(self):
        return self.name


class sayhi(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=False,editable=False)
    def __str__(self):
        return self.name