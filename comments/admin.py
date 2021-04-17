from django.contrib import admin
from .models import QuestionComment, AnswerComment


class QuestionComment_admin(admin.ModelAdmin):
    readonly_fields = ('id',)


class AnswerComment_admin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(QuestionComment, QuestionComment_admin)
admin.site.register(AnswerComment, AnswerComment_admin)