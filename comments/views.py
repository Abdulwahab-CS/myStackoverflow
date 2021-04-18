
# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# models
from .models import QuestionComment, AnswerComment

# serializers
from .serializers import QuestionCommentSerializer, AnswerCommentSerializer
from .serializers import QuestionCommentUpdateSerializer, AnswerCommentUpdateSerializer

# others
from django.http import Http404


class QuestionCommentList(APIView):
    """
        POST : to create a comment on a question
    """

    def post(self, request, format=None):
        serializer = QuestionCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionCommentDetail(APIView):
    """
        GET : to retrieve a question comment\n
        PATCH : to update a question comment\n
        DELETE : to delete a question comment
    """

    def get_object(self, pk):
        try:
            return QuestionComment.objects.get(pk=pk)
        except QuestionComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = QuestionCommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = QuestionCommentUpdateSerializer(comment, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'question comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class AnswerCommentList(APIView):
    """
        POST : to create a comment on an answer
    """

    def post(self, request, format=None):
        serializer = AnswerCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerCommentDetail(APIView):
    """
        GET : to retrieve an asnwer comment\n
        PATCH : to update an asnwer comment\n
        DELETE : to delete an asnwer comment
    """

    def get_object(self, pk):
        try:
            return AnswerComment.objects.get(pk=pk)
        except AnswerComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = AnswerCommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = AnswerCommentUpdateSerializer(comment, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'answer comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)