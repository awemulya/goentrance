from django.contrib import admin

from .models import *

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Chapter)
admin.site.register(QuestionSet)
admin.site.register(Question)
