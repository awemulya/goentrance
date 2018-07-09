from . import views
from rest_framework import routers
from django.conf.urls import url

from django.urls import path, include
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView,\
	SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView



urlpatterns = [
	path('', CourseListView.as_view(), name='course_list'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('edit/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
	path('', SubjectListView.as_view(), name='subject_list'),
    path('detail/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('add/', SubjectCreateView.as_view(), name='subject_add'),
    path('edit/<int:pk>/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
]
