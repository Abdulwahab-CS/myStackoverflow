from django.contrib import admin
from .models import Question, Tag


class Question_(admin.ModelAdmin):
    readonly_fields = ('id',)


class Tag_(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Question, Question_)
admin.site.register(Tag, Tag_)
