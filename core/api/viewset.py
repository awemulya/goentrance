from rest_framework import viewsets

from core.models import Chapter, Course, Question, QuestionSet, QuickNotes, Subject, Syllabus, Videos, Unit, Options
from .serializers import ChapterSerializer, CourseSerializer, QuestionSerializer, QuestionSetSerializer, QuickNotesSerializer,\
    SubjectSerializer, SyllabusSerializer, VideosSerializer, UnitSerializer, OptionsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SyllabusViewSet(viewsets.ModelViewSet):
    serializer_class = SyllabusSerializer
    queryset = Syllabus.objects.all()


class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class QuestionSetViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSetSerializer
    queryset = QuestionSet.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuickNotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuickNotesSerializer
    queryset = QuickNotes.objects.all()


class VideosViewSet(viewsets.ModelViewSet):
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()


class OptionsViewSet(viewsets.ModelViewSet):
    serializer_class = OptionsSerializer
    queryset = Options.objects.all()
