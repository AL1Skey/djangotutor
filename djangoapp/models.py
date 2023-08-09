from django.db import models

# Create your models here.      
class Profile(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    details=models.CharField(max_length=500)
    
    # Naming created database according to name variable
    def __str__(self):
        return self.name
    