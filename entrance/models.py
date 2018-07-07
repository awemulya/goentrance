from django.contrib.auth.models import User
from django.db import models

from core.models import Question, Options


class Entrance(models.Model):
    user = models.ForeignKey(User, related_name="entrances", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time_seconds = models.IntegerField(default=0)


class EntranceQuestions(models.Model):
    entrance = models.ForeignKey(Entrance, related_name="entrance_questions")
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Options)