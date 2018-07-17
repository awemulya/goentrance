# from django.http import HttpResponseRidirect
# from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .models import Course, Subject, Unit, Chapter
from django.urls import reverse_lazy
from .forms import CourseCreateForm, SubjectCreateForm, UnitCreateForm, ChapterCreateForm


# Create your views here.
class CoresDashboardView(TemplateView):
    template_name = 'core/cores_dashboard.html'

class CourseListView(ListView):
	model = Course
	template_name = 'core/course_list.html'


class CourseDetailView(DetailView):
	model = Course
	template_name = 'core/course_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['subjects'] = Subject.objects.filter(course_id=self.kwargs['pk'])
		return context


class CourseCreateView(CreateView):
	model = Course
	#fields = ('name',)
	form_class = CourseCreateForm
	template_name = 'core/course_form.html'
	success_url = reverse_lazy('core:course_list')


class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'core/course_form.html'
	fields = ('name',)
	success_url = reverse_lazy('core:course_list')


class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'core/course_delete.html'
	success_url = reverse_lazy('core:course_list')


class SubjectListView(ListView):
	model = Subject
	template_name = 'core/subject_list.html'


class SubjectDetailView(DetailView):
	model = Subject
	template_name = 'core/subject_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['units'] = Unit.objects.filter(subject_id=self.kwargs['pk'])
		return context


class SubjectCreateView(CreateView):
	model = Subject
	#fields = ('name', 'course',)
	form_class = SubjectCreateForm
	template_name = 'core/subject_form.html'
	success_url = reverse_lazy('core:subject_list')


class SubjectUpdateView(UpdateView):
	model = Subject
	template_name = 'core/subject_form.html'
	fields = ('name', 'course',)
	success_url = reverse_lazy('core:subject_list')


class SubjectDeleteView(DeleteView):
	model = Subject
	template_name = 'core/subject_delete.html'
	success_url = reverse_lazy('core:subject_list')


class UnitListView(ListView):
	model = Unit
	template_name = 'core/unit_list.html'


class UnitDetailView(DetailView):
	model = Unit
	template_name = 'core/unit_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['chapters'] = Chapter.objects.filter(unit_id=self.kwargs['pk'])
		return context


class UnitCreateView(CreateView):
	model = Unit
	#fields = ('name', 'subject',)
	form_class = UnitCreateForm
	template_name = 'core/unit_form.html'
	success_url = reverse_lazy('core:unit_list')


class UnitUpdateView(UpdateView):
	model = Unit
	template_name = 'core/unit_form.html'
	fields = ('name', 'subject',)
	success_url = reverse_lazy('core:unit_list')


class UnitDeleteView(DeleteView):
	model = Unit
	template_name = 'core/unit_delete.html'
	success_url = reverse_lazy('core:unit_list')


class ChapterListView(ListView):
	model = Chapter
	template_name = 'core/chapter_list.html'


class ChapterDetailView(DetailView):
	model = Chapter
	template_name = 'core/chapter_detail.html'


class ChapterCreateView(CreateView):
	model = Chapter
	#fields = ('name', 'unit',)
	form_class = ChapterCreateForm
	template_name = 'core/chapter_form.html'
	success_url = reverse_lazy('core:chapter_list')


class ChapterUpdateView(UpdateView):
	model = Chapter
	template_name = 'core/chapter_form.html'
	fields = ('name', 'unit',)
	success_url = reverse_lazy('core:chapter_list')


class ChapterDeleteView(DeleteView):
	model = Chapter
	template_name = 'core/chapter_delete.html'
	success_url = reverse_lazy('core:chapter_list')


class SubjectUnitView(TemplateView):
	template_name = 'core/subject_unit.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['subject'] = Subject.objects.get(id=self.kwargs['subject_pk'])
		context['subject_unit'] = Unit.objects.filter(subject_id=self.kwargs['subject_pk'])
		context['chapters'] = Chapter.objects.filter(unit__subject_id=self.kwargs['subject_pk'])
		return context