from django.contrib import admin

from .models import *

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Chapter)
admin.site.register(QuestionSet)

class OptionInline(admin.StackedInline):
    model = Options
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',               {'fields': ['question', 'question_set']}),
    ]
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)

