from django.contrib import admin
from .models import Answer


class Answer_(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Answer, Answer_)
