# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# models
from .models import Answer

# serializers
from .serializers import AnswerSerializer, AnswerFullSerializer, AnswerUpdateSerializer

# others
from django.http import Http404


class AnswerList(APIView):
    """
        POST : to create a new answer
    """

    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetail(APIView):
    """
        GET : to retrieve an answer
        PATCH : to update an answer
        DELETE : to delete an answer
    """

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerFullSerializer(answer)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerUpdateSerializer(answer, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        answer = self.get_object(pk)
        answer.delete()
        return Response({'message': 'answer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)