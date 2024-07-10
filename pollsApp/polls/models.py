from django.db import models

# Create my models here and defining the str method
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # defining a str method
    def __str__(self):
            return self.question_text
        
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
        
    # defining a str method
    def __str__(self):
            return self.choice_text
            
            
