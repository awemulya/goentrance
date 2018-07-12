from django import forms
from .models import Course, Subject, Unit, Chapter

class CourseCreateForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('name',)


class SubjectCreateForm(forms.ModelForm):

	class Meta:
		model = Subject
		fields = ('name', 'course',)


class UnitCreateForm(forms.ModelForm):

	class Meta:
		model = Unit
		fields = ('name', 'subject',)
			

class ChapterCreateForm(forms.ModelForm):

	class Meta:
		model = Chapter
		fields = ('name', 'unit',)