from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.email

