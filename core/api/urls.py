from django.urls import path, include

from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

router.register(r'users', viewset.UserViewSet)
router.register(r'tokens', viewset.TokenViewSet)
router.register(r'courses', viewset.CourseViewSet, base_name='courses')
router.register(r'chapters', viewset.ChapterViewSet, base_name='chapters')
router.register(r'syllabus', viewset.SyllabusViewSet, base_name='syllabus')
router.register(r'units', viewset.UnitViewSet, base_name='units')
router.register(r'question-sets', viewset.QuestionSetViewSet, base_name='question_sets')
router.register(r'questions', viewset.QuestionViewSet, base_name='questions')
router.register(r'quick-notes', viewset.QuickNotesViewSet, base_name='quick_notes')
router.register(r'videos', viewset.VideosViewSet, base_name='videos')
router.register(r'options', viewset.OptionsViewSet, base_name='options')
router.register(r'entrance', viewset.EntranceViewSet, base_name='entrance')
router.register(r'entrance-questions', viewset.EntranceQuestionsViewSet, base_name='entrance_questions')
router.register(r'package', viewset.PackageViewSet, base_name='package')


urlpatterns = [
    path('', include(router.urls)),
    path('course-subjects/', viewset.CourseSubjectsViewSet.as_view({'get': 'list', }), name="course_subject"),

]
