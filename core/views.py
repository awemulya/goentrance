from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import reverse, get_object_or_404

from .models import Course, Subject, Unit, Chapter
from .forms import CourseCreateForm, SubjectCreateForm, UnitCreateForm, ChapterCreateForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class SuperAdminMixin(LoginRequiredMixin):
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      if request.user.is_superuser:
        return super(SuperAdminMixin, self).dispatch(request, *args, **kwargs)
    return HttpResponseRedirect('/accounts/login')


# Create your views here.
class CoresDashboardView(SuperAdminMixin, TemplateView):
  template_name = 'core/cores_dashboard.html'

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      if request.user.is_superuser:
        return super(SuperAdminMixin, self).dispatch(request, *args, **kwargs)

      else:
        return HttpResponseRedirect('/spa#/')

    return HttpResponseRedirect('/accounts/login')


class CourseListView(SuperAdminMixin, ListView):
  model = Course
  template_name = 'core/course_list.html'


class CourseDetailView(SuperAdminMixin, DetailView):
  model = Course
  template_name = 'core/course_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['subjects'] = Subject.objects.filter(course_id=self.kwargs['pk'])
    return context


class CourseCreateView(SuperAdminMixin, CreateView):
  model = Course
  # fields = ('name',)
  form_class = CourseCreateForm
  template_name = 'core/course_form.html'
  success_url = reverse_lazy('core:course_list')


class CourseUpdateView(SuperAdminMixin, UpdateView):
  model = Course
  template_name = 'core/course_form.html'
  fields = ('name',)
  success_url = reverse_lazy('core:course_list')


class CourseDeleteView(SuperAdminMixin, DeleteView):
  model = Course
  template_name = 'core/course_delete.html'
  success_url = reverse_lazy('core:course_list')


class SubjectListView(SuperAdminMixin, ListView):
  model = Subject
  template_name = 'core/subject_list.html'


class SubjectDetailView(SuperAdminMixin, DetailView):
  model = Subject
  template_name = 'core/subject_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['units'] = Unit.objects.filter(subject_id=self.kwargs['pk'])
    return context


class SubjectCreateView(SuperAdminMixin, CreateView):
  model = Subject
  # fields = ('name', 'course',)
  form_class = SubjectCreateForm
  template_name = 'core/subject_form.html'
  success_url = reverse_lazy('core:subject_list')

  def form_valid(self, form):
    form.instance.course = get_object_or_404(Course, pk=self.kwargs['pk'])
    form.save()
    return super().form_valid(form)


class SubjectUpdateView(SuperAdminMixin, UpdateView):
  model = Subject
  template_name = 'core/subject_form.html'
  fields = ('name', 'course',)
  success_url = reverse_lazy('core:subject_list')


class SubjectDeleteView(SuperAdminMixin, DeleteView):
  model = Subject
  template_name = 'core/subject_delete.html'
  success_url = reverse_lazy('core:subject_list')


class UnitListView(SuperAdminMixin, ListView):
  model = Unit
  template_name = 'core/unit_list.html'


class UnitDetailView(SuperAdminMixin, DetailView):
  model = Unit
  template_name = 'core/unit_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['chapters'] = Chapter.objects.filter(unit_id=self.kwargs['pk'])
    return context


class UnitCreateView(SuperAdminMixin, CreateView):
  model = Unit
  # fields = ('name', 'subject',)
  form_class = UnitCreateForm
  template_name = 'core/unit_form.html'
  success_url = reverse_lazy('core:unit_list')

  def form_valid(self, form):
    form.instance.subject = get_object_or_404(Subject, pk=self.kwargs['pk'])
    form.save()
    return super().form_valid(form)


class UnitUpdateView(SuperAdminMixin, UpdateView):
  model = Unit
  template_name = 'core/unit_form.html'
  fields = ('name', 'subject',)
  success_url = reverse_lazy('core:unit_list')


class UnitDeleteView(SuperAdminMixin, DeleteView):
  model = Unit
  template_name = 'core/unit_delete.html'
  success_url = reverse_lazy('core:unit_list')


class ChapterListView(SuperAdminMixin, ListView):
  model = Chapter
  template_name = 'core/chapter_list.html'


class ChapterDetailView(SuperAdminMixin, DetailView):
  model = Chapter
  template_name = 'core/chapter_detail.html'


class ChapterCreateView(SuperAdminMixin, CreateView):
  model = Chapter
  # fields = ('name', 'unit',)
  form_class = ChapterCreateForm
  template_name = 'core/chapter_form.html'

  def form_valid(self, form):
    form.instance.unit = get_object_or_404(Unit, pk=self.kwargs['pk'])
    form.save()
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy('core:unit_detail', args=(self.kwargs['pk'],))


class ChapterUpdateView(SuperAdminMixin, UpdateView):
  model = Chapter
  template_name = 'core/chapter_form.html'
  fields = ('name', 'unit',)
  success_url = reverse_lazy('core:chapter_list')


class ChapterDeleteView(SuperAdminMixin, DeleteView):
  model = Chapter
  template_name = 'core/chapter_delete.html'
  success_url = reverse_lazy('core:chapter_list')


class SubjectUnitView(SuperAdminMixin, TemplateView):
  template_name = 'core/subject_unit.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['subject'] = Subject.objects.get(id=self.kwargs['subject_pk'])
    context['subject_unit'] = Unit.objects.filter(subject_id=self.kwargs['subject_pk'])
    # context['chapters'] = Chapter.objects.filter(unit__subject_id=self.kwargs['subject_pk'])
    return context


class SignUp(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'core/signup.html'
