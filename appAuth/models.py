from django.db import models
   
class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField(max_length=200)

        def __str__(self):
                return self.name
        

        