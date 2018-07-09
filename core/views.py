# from django.http import HttpResponseRidirect
# from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Course, Subject
from django.urls import reverse_lazy
from .forms import CourseCreateForm, SubjectCreateForm


# Create your views here.

class CourseListView(ListView):
	model = Course
	template_name = 'core/course_list.html'


class CourseDetailView(DetailView):
	model = Course
	template_name = 'core/course_detail.html'


class CourseCreateView(CreateView):
	model = Course
	#fields = ('name',)
	form_class = CourseCreateForm
	template_name = 'core/course_form.html'
	success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'core/course_form.html'
	fields = ('name',)
	success_url = reverse_lazy('course_list')


class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'core/course_delete.html'
	success_url = reverse_lazy('course_list')


class SubjectListView(ListView):
	model = Subject
	template_name = 'core/subject_list.html'


class SubjectDetailView(DetailView):
	model = Subject
	template_name = 'core/subject_detail.html'


class SubjectCreateView(CreateView):
	model = Subject
	#fields = ('name',)
	form_class = SubjectCreateForm
	template_name = 'core/subject_form.html'
	success_url = reverse_lazy('subject_list')


class SubjectUpdateView(UpdateView):
	model = Subject
	template_name = 'core/subject_form.html'
	fields = ('name',)
	success_url = reverse_lazy('subject_list')


class SubjectDeleteView(DeleteView):
	model = Subject
	template_name = 'core/subject_delete.html'
	success_url = reverse_lazy('subject_list')