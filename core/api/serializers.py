from rest_framework import serializers

from core.models import Chapter, Course, Question, QuestionSet, QuickNotes, Subject, Syllabus, Videos, Unit, Options
from entrance.models import Entrance, EntranceQuestions
from package.models import Package, Tokens


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        exclude = ()


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ()


class CourseDetailSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Course
        exclude = ()


# class SubjectUnitChaptersSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Subject
#         exclude = ()


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('id', 'name', 'subject', 'unit_chapters',)


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        exclude = ()


class SyllabusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Syllabus
        exclude = ()


class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Videos
        exclude = ()


class QuickNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickNotes
        exclude = ()


class QuestionSetSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    questions_count = serializers.ReadOnlyField()

    class Meta:
        model = QuestionSet
        fields = ('id', 'type', 'name', 'chapter', 'time', 'questions_count')


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        exclude = ('question', 'correct')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True)

    class Meta:
        model = Question
        exclude = ()


class EntranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrance
        exclude = ()


class EntranceQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntranceQuestions
        exclude = ()


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        exclude = ()


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tokens
        fields = ('activated_date', 'package', 'user')
