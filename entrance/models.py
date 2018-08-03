from django.contrib.auth.models import User
from django.db import models

from core.models import Question, Options


class Entrance(models.Model):
    user = models.ForeignKey(User, related_name="entrances", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time_seconds = models.IntegerField(default=0)
    # question set

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user


class EntranceQuestions(models.Model):
    entrance = models.ForeignKey(Entrance, related_name="entrance_questions", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE)

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question
