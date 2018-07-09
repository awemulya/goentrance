from . import views
from rest_framework import routers
from django.conf.urls import url

from django.urls import path, include
from .views import CoresDashboardView, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView,\
	SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView


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
    path('subject-add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject-edit/<int:pk>/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject-delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
]
