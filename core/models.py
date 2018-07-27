from django.db import models

QUESTION_SET_CHOICES = [(0, "Past Questions"), (1, "Mock Sets")]


class Course(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, related_name="subjects",  on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=250)
    subject = models.ForeignKey(Subject, related_name="units",  on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def unit_chapters(self):
        return self.chapters.values('name', 'id')


class Chapter(models.Model):
    name = models.CharField(max_length=250)
    unit = models.ForeignKey(Unit, related_name="chapters",  on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Syllabus(models.Model):
    unit = models.ForeignKey(Unit, related_name="syllabuslist", on_delete=models.CASCADE)
    syllabus = models.TextField()

    class Meta:
        ordering = ['syllabus']

    def __str__(self):
        return self.syllabus


class Videos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    chapter = models.ForeignKey(Chapter, related_name="videos", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class QuickNotes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    notes = models.TextField()
    chapter = models.ForeignKey(Chapter, related_name="quicknotes", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class QuestionSet(models.Model):
    type = models.IntegerField(default=0, choices=QUESTION_SET_CHOICES)
    name = models.CharField(max_length=64)
    chapter = models.ForeignKey(Chapter, related_name="sets", on_delete=models.CASCADE)
    time = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    question_set = models.ForeignKey(QuestionSet, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    answer = models.CharField(max_length=250)

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question
