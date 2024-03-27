from django.db import models

# J'ai definie le user model
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
