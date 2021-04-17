from rest_framework import serializers
from .models import Answer
from comments.models import AnswerComment
from comments.serializers import AnswerCommentSerializer

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ['id', 'body', 'question_id']


class AnswerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['body']

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        ser = AnswerSerializer(instance)
        return ser.data


class AnswerFullSerializer(serializers.ModelSerializer):
    
    comments = serializers.SerializerMethodField('get_comments_')

    class Meta:
        model = Answer
        fields = ['id', 'body', 'question_id', 'comments']

    def get_comments_(self, answer):
        comments = AnswerComment.objects.filter(answer_id=answer)
        ser = AnswerCommentSerializer(comments, many=True)
        return ser.data