# encoding: utf-8
from django.db import models
from datetime import datetime


class User(models.Model):
    Username = models.CharField(max_length=250, blank=False)
    Email = models.EmailField(blank=True)
    Genre = models.CharField(max_length=20, blank=False)
    Autonomous_community = models.CharField(max_length=250, blank=False)
    Age = models.PositiveIntegerField()

    def __unicode__(self):
        return self.username + " " + self.email


class Vote(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    id_poll = models.IntegerField(blank=False)
    age = models.PositiveIntegerField()
    genre = models.CharField(max_length=20, blank=False)
    autonomous_community = models.CharField(max_length=250, blank=False)
    answers = models.TextField(blank=False)

    def __unicode__(self):
        return str(self.id) + " " + str(self.id_poll) + str(
            self.age) + " " + self.genre + " " + self.autonomous_community + " " + self.answers


class Poll(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    title = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=250, blank=False)
    startDate = models.DateField()
    endDate = models.DateField()
#     questions = models.ManyToManyField("Question")
    
#     def __init__(self, id, title, description, startDate, endDate, questions):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.startDate = datetime.strptime(startDate, '%d-%m-%Y').date()
#         self.endDate = datetime.strptime(endDate, '%d-%m-%Y').date()
#         self.questions = questions

    def __unicode__(self):
        return str(self.id) + " " + str(self.title)


class Question(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    text = models.CharField(max_length=250, blank=False)
    poll = models.ForeignKey(Poll)
    
#     def __init__(self, id, text):
#         self.id = id
#         self.text = text
#         self.poll = poll

    def __unicode__(self):
        return str(self.id) + " " + str(self.text) + " " + str(self.questions)