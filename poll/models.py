from django.db import models

# Create your models here.
class Polls(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)


    def __str__(self):
        return self.question