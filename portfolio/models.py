from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank=True) #blank = true means you can keep it blank if you want can be done in other fields
    
    def __str__(self):
        return self.title
    