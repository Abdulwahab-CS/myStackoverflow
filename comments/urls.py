from django.urls import path
from .views import QuestionCommentList, AnswerCommentList
from .views import QuestionCommentDetail, AnswerCommentDetail

urlpatterns = [

    path('question_comments/', QuestionCommentList.as_view()),
    path('answer_comments/', AnswerCommentList.as_view()),

    path('question_comments/<int:pk>/', QuestionCommentDetail.as_view()),
    path('answer_comments/<int:pk>/', AnswerCommentDetail.as_view()),
]