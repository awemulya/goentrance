from django import forms
from .models import Course, Subject

class CourseCreateForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('name',)


class SubjectCreateForm(forms.ModelForm):

	class Meta:
		model = Subject
		fields = ('name', 'course',)
			