from rest_framework import serializers
from .models import QuestionComment, AnswerComment


class QuestionCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionComment
        fields = ['id', 'body', 'question_id']


class QuestionCommentUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionComment
        fields = ['body']

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        ser = QuestionCommentSerializer(instance)
        return ser.data


class AnswerCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerComment
        fields = ['id', 'body', 'answer_id']


class AnswerCommentUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerComment
        fields = ['body']

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        ser = AnswerCommentSerializer(instance)
        return ser.data
