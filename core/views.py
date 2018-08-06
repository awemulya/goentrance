from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Course, Subject, Unit, Chapter, QuestionSet, Question, Options
from .forms import CourseCreateForm, SubjectCreateForm, UnitCreateForm, ChapterCreateForm
from django.views import generic


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

    def get_context_data(self, **kwargs):
        context = super(CoresDashboardView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all().count()
        context['users'] = User.objects.all().count()
        return context


class CourseListView(SuperAdminMixin, ListView):
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(SuperAdminMixin, DetailView):
    model = Course
    template_name = 'core/course_detail.html'
    context_object_name = 'course'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, id=self.kwargs['course_id'])
        return context


class SubjectUpdateView(SuperAdminMixin, UpdateView):
    model = Subject
    template_name = 'core/subject_form.html'
    form_class = SubjectCreateForm

    def get_success_url(self):
        return reverse_lazy('core:course_detail', args=(self.object.course.id,))


class SubjectDeleteView(SuperAdminMixin, DeleteView):
    model = Subject
    template_name = 'core/subject_delete.html'

    def get_success_url(self):
      return reverse_lazy('core:course_detail', args=(self.object.course.id,))


class UnitDetailView(SuperAdminMixin, DetailView):
    model = Unit
    template_name = 'core/unit_detail.html'
    context_object_name = 'unit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = Chapter.objects.filter(unit_id=self.kwargs['pk'])
        return context


class UnitCreateView(SuperAdminMixin, CreateView):
    model = Unit
    form_class = UnitCreateForm
    template_name = 'core/unit_form.html'

    def form_valid(self, form):
        form.instance.subject = get_object_or_404(Subject, pk=self.kwargs['subject_id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:subject_detail', args=(self.kwargs['subject_id'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs['subject_id']
        context['subject'] = get_object_or_404(Subject, id=subject_id)
        context['course'] = get_object_or_404(Course, subjects=subject_id)

        return context


class UnitUpdateView(SuperAdminMixin, UpdateView):
    model = Unit
    template_name = 'core/unit_form.html'
    form_class = UnitCreateForm

    def get_success_url(self):
        return reverse_lazy('core:subject_detail', args=(self.object.subject.id,))


class UnitDeleteView(SuperAdminMixin, DeleteView):
    model = Unit
    template_name = 'core/unit_delete.html'

    def get_success_url(self):
        return reverse_lazy('core:subject_detail', args=(self.object.subject.id,))


class ChapterCreateView(SuperAdminMixin, CreateView):
    model = Chapter
    form_class = ChapterCreateForm
    template_name = 'core/chapter_form.html'

    def form_valid(self, form):
        form.instance.unit = get_object_or_404(Unit, pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unit_id = self.kwargs['pk']
        # context['subject'] = get_object_or_404(Subject, id=subject_id)
        context['unit'] = get_object_or_404(Unit, id=unit_id)

        return context

    def get_success_url(self):
        return reverse_lazy('core:unit_detail', args=(self.kwargs['pk'],))


class ChapterUpdateView(SuperAdminMixin, UpdateView):
    model = Chapter
    template_name = 'core/chapter_form.html'
    form_class = ChapterCreateForm

    def get_success_url(self):
        return reverse_lazy('core:unit_detail', args=(self.object.unit.id,))


class ChapterDeleteView(SuperAdminMixin, DeleteView):
    model = Chapter
    template_name = 'core/chapter_delete.html'
    success_url = reverse_lazy('core:chapter_list')

    def get_success_url(self):
        return reverse_lazy('core:unit_detail', args=(self.object.unit.id,))


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionSetsFormView, self).get_context_data(**kwargs)
        context['chapter'] = get_object_or_404(Chapter, id=self.kwargs['chapter_id'])
        return context


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


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'core/user_profile.html'


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    context_object_name = 'user'
    template_name = 'core/user_profile_update.html'

    def get_success_url(self):
        success_url = reverse_lazy('core:user_profile', args=(self.object.pk,))
        return success_url
