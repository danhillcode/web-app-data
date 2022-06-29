from django.db import models
from django.contrib.auth.models import User # importing users   
from django.db.models.deletion import CASCADE, DO_NOTHING
from traitlets import default 


class Demo(models.Model):
    demo_title = models.CharField(max_length=200)
    demo_description = models.CharField(max_length=200)

    def __str__(self):
        return self.demo_title


# Model for questions
class Question(models.Model):
    photo = models.ImageField(upload_to='images',blank = True,null = True)
    title = models.CharField(max_length=500)
    

class Answer(models.Model):
    answer = models.TextField()
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING) #User (student)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING) # question