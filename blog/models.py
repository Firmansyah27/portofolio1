from django.db import models

# Create A Blog models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    comment = models.TextField()
    image = models.ImageField(upload_to='images/')

#Create a migration

#Migrate

#Add to the admin
