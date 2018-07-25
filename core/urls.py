from . import views
from rest_framework import routers


from django.urls import path, include
from .views import CoresDashboardView, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
	SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView, \
    UnitListView, UnitDetailView, UnitCreateView, UnitUpdateView, UnitDeleteView, \
    ChapterListView, ChapterDetailView, ChapterCreateView, ChapterUpdateView, ChapterDeleteView, \
    SubjectUnitView


app_name = 'core'

urlpatterns = [
    path('', CoresDashboardView.as_view(), name='cores_dashboard'),
    path('course-list', CourseListView.as_view(), name='course_list'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course-add/', CourseCreateView.as_view(), name='course_add'),
    path('course-edit/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('course-delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
	path('subject-list', SubjectListView.as_view(), name='subject_list'),
    path('subject-detail/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject-add/<int:pk>/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject-edit/<int:pk>/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject-delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('unit-list', UnitListView.as_view(), name='unit_list'),
    path('unit-detail/<int:pk>/', UnitDetailView.as_view(), name='unit_detail'),
    path('unit-add/<int:pk>/', UnitCreateView.as_view(), name='unit_add'),
    path('unit-edit/<int:pk>/', UnitUpdateView.as_view(), name='unit_edit'),
    path('unit-delete/<int:pk>/', UnitDeleteView.as_view(), name='unit_delete'),
    path('chapter-list', ChapterListView.as_view(), name='chapter_list'),
    path('chapter-detail/<int:pk>/', ChapterDetailView.as_view(), name='chapter_detail'),
    path('chapter-add/<int:pk>', ChapterCreateView.as_view(), name='chapter_add'),
    path('chapter-edit/<int:pk>/', ChapterUpdateView.as_view(), name='chapter_edit'),
    path('chapter-delete/<int:pk>/', ChapterDeleteView.as_view(), name='chapter_delete'),
    path('subject-unit/<int:subject_pk>', SubjectUnitView.as_view(), name='subject_unit'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
