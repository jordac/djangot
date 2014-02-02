from django.db import models
from models import Model

class Poll(Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
