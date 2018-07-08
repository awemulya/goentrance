# from django.http import HttpResponseRidirect
# from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Course
from django.urls import reverse_lazy
from .forms import CourseCreateForm


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