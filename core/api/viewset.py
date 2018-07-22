from django.contrib.auth.models import User

from rest_framework import viewsets, serializers

from core.models import Chapter, Course, Question, QuestionSet, QuickNotes, Subject, Syllabus, Videos, Unit, Options
from entrance.models import Entrance, EntranceQuestions
from package.models import Package, Tokens
from .serializers import ChapterSerializer, CourseSerializer, QuestionSerializer, QuestionSetSerializer, QuickNotesSerializer,\
    SubjectSerializer, SyllabusSerializer, VideosSerializer, UnitSerializer, OptionsSerializer, EntranceSerializer, \
    EntranceQuestionsSerializer, PackageSerializer, TokenSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Tokens.objects.all()
    serializer_class = TokenSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSubjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class SubjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        course_id = self.kwargs.get('course')
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class SyllabusViewSet(viewsets.ModelViewSet):
    serializer_class = SyllabusSerializer
    queryset = Syllabus.objects.all()


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


class EntranceViewSet(viewsets.ModelViewSet):
    serializer_class = EntranceSerializer
    queryset = Entrance.objects.all()


class EntranceQuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = EntranceQuestionsSerializer
    queryset = EntranceQuestions.objects.all()


class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

