from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    comment = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.comment[:100]
    def date_new (self):
        return self.date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
