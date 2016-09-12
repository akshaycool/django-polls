from __future__ import unicode_literals

from django.db import models

CHOICES = ['YES', 'NO']

# class Poll(models.Model):
#     #question-textfield vote_status-choicefield(yes/no)
#     created=models.DateTimeField(auto_now_add=True)
#     question=models.CharField(max_length=100,blank=True,default='')
#     vote_status=models.CharField(choices=CHOICES,default='YES',max_length=5)
#     owner=models.ForeignKey('auth.User',related_name='polls')

# class Meta:
#     ordering=('created',)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    poll_count = models.IntegerField(default=0)
