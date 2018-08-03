from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import reverse, get_object_or_404

from .models import Course, Subject, Unit, Chapter, QuestionSet, Question, Options
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
        context = super(CourseDetailView, self).get_context_data(**kwargs)
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
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.filter(course_id=self.kwargs['course_id'])


class SubjectDetailView(SuperAdminMixin, DetailView):
    model = Subject
    template_name = 'core/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['units'] = Unit.objects.filter(subject_id=self.kwargs['pk'])
        return context


class SubjectCreateView(SuperAdminMixin, CreateView):
    model = Subject
    form_class = SubjectCreateForm
    template_name = 'core/subject_form.html'

    def form_valid(self, form):
        form.instance.course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        form.save()
        return super(SubjectCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:course_detail', args=(self.kwargs['course_id'],))


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


class QuestionSetsListView(SuperAdminMixin, ListView):
    template_name = 'core/question_sets.html'
    model = QuestionSet
    context_object_name = 'question_sets'

    def get_queryset(self):
        return QuestionSet.objects.filter(chapter_id=self.kwargs['chapter_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionSetsListView, self).get_context_data(**kwargs)
        context['chapter'] = get_object_or_404(Chapter, id=self.kwargs['chapter_id'])
        return context


class QuestionSetsFormView(SuperAdminMixin, CreateView):
    template_name = 'core/question_sets_form.html'
    model = QuestionSet
    fields = ('type', 'name', 'time')

    def form_valid(self, form):
        form.instance.chapter = get_object_or_404(Chapter, pk=self.kwargs['chapter_id'])
        form.save()
        return super(QuestionSetsFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:question_sets', args=(self.kwargs['chapter_id'],))


class QuestionSetsUpdateView(SuperAdminMixin, UpdateView):
    template_name = 'core/question_sets_form.html'
    model = QuestionSet
    fields = ('type', 'name', 'time')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(QuestionSetsListView, self).get_context_data(**kwargs)
    #     context['chapter'] = get_object_or_404(Chapter, id=self.kwargs['chapter_id'])
    #     return context

    def form_valid(self, form):
        form.instance.chapter = get_object_or_404(Chapter, pk=self.object.chapter.id)
        form.save()
        return super(QuestionSetsUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:question_sets', args=(self.object.chapter.id,))


class QuestionSetsDeleteView(SuperAdminMixin, DeleteView):
    template_name = 'core/question_sets_delete.html'
    model = QuestionSet
    context_object_name = 'question_sets'

    def get_success_url(self):
        return reverse_lazy('core:question_sets', args=(self.object.chapter.id,))


class QuestionSetsDashboard(DetailView):
  model = QuestionSet
  context_object_name = 'obj'


  def get_context_data(self, **kwargs):
      context = super(QuestionSetsDashboard, self).get_context_data(**kwargs)
      question_set = context.get('obj')
      questions = question_set.questions.all()
      context['questions'] = questions
      return context

class QuestionAddView(SuperAdminMixin, CreateView):
    template_name = 'core/question_form.html'
    model = Question
    fields = ('question',)

    def form_valid(self, form):
        form.instance.question_set = get_object_or_404(QuestionSet, pk=self.kwargs['pk'])
        form.save()
        return super(QuestionAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:question_set_dashboard', args=(self.kwargs['pk'],))

class QuestionDashboardView(SuperAdminMixin, DetailView):
    template_name = "core/question_dashboard.html"
    model = Question

    def get_context_data(self, **kwargs):
        data = super(QuestionDashboardView, self).get_context_data(**kwargs)
        data['options'] = Options.objects.filter(question__id=self.kwargs['pk'])
        return data


class OptionDetailView(SuperAdminMixin, UpdateView):
    model = Options
    fields = ('answer', 'correct')

    def get_success_url(self):
        option = Options.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('core:question_dashboard', args=(option.question.id,))


class OptionAddView(SuperAdminMixin, CreateView):
    model = Options
    fields = ('answer', 'correct')

    def form_valid(self, form):
        form.instance.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        form.save()
        return super(OptionAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:question_dashboard', args=(self.kwargs['pk'],))


class SignUp(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'core/signup.html'
