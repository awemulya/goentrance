from django.db import models

QUESTION_SET_CHOICES = [(0, "Past Questions"), (1, "Mock Sets")]

class Course(models.Model):
    name = models.CharField()


class Subject(models.Model):
    name = models.CharField()
    course = models.ForeignKey(Course, related_name="subjects",  on_delete=models.CASCADE)


class Unit(models.Model):
    name = models.CharField()
    subject = models.ForeignKey(Subject, related_name="units",  on_delete=models.CASCADE)


class Chapter(models.Model):
    name = models.CharField()
    chapter = models.ForeignKey(Unit, related_name="chapters",  on_delete=models.CASCADE)


class Syllabus(models.model):
    unit = models.ForeignKey(Unit, related_name="syllabuslist", on_delete=models.CASCADE)
    syllabus = models.TextField()


class Videos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    chapter = models.ForeignKey(Chapter, related_name="videos", on_delete=models.CASCADE)


class QuickNotes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    notes = models.TextField()
    chapter = models.ForeignKey(Chapter, related_name="quicknotes", on_delete=models.CASCADE)


class QuestionSet(models.Model):
    type = models.IntegerField(default=0, choices=QUESTION_SET_CHOICES)
    name = models.CharField(max_length=64)
    chapter = models.ForeignKey(Chapter, related_name="sets", on_delete=models.CASCADE)


class Question(models.Model):
    question_set = models.ForeignKey(QuestionSet, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()


class Options(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    answer = models.CharField()