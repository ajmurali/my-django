from django.db import models
from sorl.thumbnail import ImageField

class Project(models.Model):
    Title = models.CharField(max_length= 150 , blank = False , null= False)
    Text = models.TextField(max_length=1000, blank = False, null = False)
    Image = models.ImageField()
    SourceCode = models.FileField(default=1)
    Demo = models.CharField(max_length= 1000 , blank = False , null= False, default=1)

    def __str__(self):
        return self.Title    
