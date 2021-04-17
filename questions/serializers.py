
from rest_framework import serializers

# models
from .models import Question, Tag
from answers.models import Answer
from comments.models import QuestionComment

# serializers
from answers.serializers import AnswerSerializer, AnswerFullSerializer
from comments.serializers import QuestionCommentSerializer

# others
from .validators import tag_validator
from .utils import *
from django.utils import timezone



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class AllQuestionsSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField('get_tags_')

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'tags']

    def get_tags_(self, question):
        ser = TagSerializer(question.tags, many=True)

        tags = []
        for item in ser.data:
            tags.append(dict(item)['name'])
        
        return tags


class QuestionCreateSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
    tags = serializers.ListField(
        child = serializers.CharField(max_length=32, validators=[tag_validator]))

    def validate_tags(self, tags):
        if len(tags) == 0:
            raise serializers.ValidationError('Enter at least one tag')
        return tags

    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']

    
    def create(self, validated_data):

        # input data
        title = validated_data.get('title')
        body = validated_data.get('body')
        tags = validated_data.get('tags')
        
        # create the question
        question = Question.objects.create(title=title, body=body)
        
        # prepare tags
        tags = lower_case_all_tags(tags)
        tags = remove_duplicate_tags(tags)

        added_tags = []
        for tag_name in tags:
            if Tag.objects.filter(name=tag_name).exists():
                tag = Tag.objects.get(name=tag_name)
            else:
                tag = Tag.objects.create(name=tag_name)
                
            added_tags.append(tag)

        # add tags to the question
        for tag in added_tags:
            question.tags.add(tag)

        question.save()

        return {
            'id': question.id,
            'title': question.title,
            'body': question.body,
            'tags': tags 
        }


class QuestionUpdateSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=255, required=False)
    body = serializers.CharField(max_length=255, required=False)
    tags = serializers.ListField(
        child = serializers.CharField(max_length=32, validators=[tag_validator]), required=False)

    def validate_tags(self, tags):
        if len(tags) == 0:
            raise serializers.ValidationError('Enter at least one tag')
        return tags

    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']


    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        

        if 'tags' in validated_data.keys():
            
            tagSerailizer = TagSerializer(instance.tags, many=True)
            
            # tags
            old_tags = get_question_tags_as_string_list(tagSerailizer.data)
            new_tags = validated_data.get('tags')

            # prepare new tags
            new_tags = lower_case_all_tags(new_tags)
            new_tags = remove_duplicate_tags(new_tags)

            # update question tags if tags are changed
            if are_tags_updated(old_tags, new_tags):
                instance.tags.clear()
                update_question_tags_list(instance, new_tags)
            

        instance.save()

        ser = AllQuestionsSerializer(instance)
        return ser.data



class QuestionFullAnswersCommentsSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField('get_tags_')
    answers = serializers.SerializerMethodField('get_answers_')
    question_comments = serializers.SerializerMethodField('get_question_comments_')

    class Meta:
        model=Question
        fields=['id', 'title', 'body', 'tags', 'question_comments', 'answers']
        
    
    def get_tags_(self, question):
        tagSerailizer = TagSerializer(question.tags, many=True)
        return get_question_tags_as_string_list(tagSerailizer.data)
    
    def get_answers_(self, question):
        answers = Answer.objects.filter(question_id=question)
        ser = AnswerFullSerializer(answers, many=True)
        return ser.data
    
    def get_question_comments_(self, question):
        comments = QuestionComment.objects.filter(question_id=question)
        ser = QuestionCommentSerializer(comments, many=True)
        return ser.data
