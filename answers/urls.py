from django.urls import path
from .views import AnswerList, AnswerDetail

urlpatterns = [

    path('', AnswerList.as_view()),
    path('<int:pk>/', AnswerDetail.as_view()),
]