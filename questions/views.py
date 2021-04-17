
# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# models
from .models import Question, Tag

# serializers
from .serializers import AllQuestionsSerializer, QuestionCreateSerializer, QuestionUpdateSerializer 
from .serializers import  QuestionFullAnswersCommentsSerializer

# others
from django.http import Http404
import re


class QuestionList(APIView):
    """
        GET : to list all questions
        POST : to create new question
    """

    def get(self, request, format=None):
        questions = self.get_queryset()
        serializer = AllQuestionsSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get_queryset(self):
        queryset = Question.objects.all()

        if 'tags' in self.request.query_params:
            tagsString = self.request.query_params.get('tags', None)
            tags = tagsString.split(',')
            queryset = Question.objects.filter(tags__name__in=tags)
        
        return queryset

class QuestionDetail(APIView):
    """
        GET : to retrieve a question
        PATCH : to update a question 
        DELETE : to delete a question
    """

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionFullAnswersCommentsSerializer(question)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionUpdateSerializer(question, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response({'message': 'answer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)