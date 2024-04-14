from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import QuizStatement, QuizQuestions, QuizInstance
from authentication.models import User


class QuizSerializer(ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    class Meta:
        model = QuizStatement
        fields = ['title', 'text', 'quiz_type', 'user_id']

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid user_id")
        else:
            raise serializers.ValidationError("user_id is required")

        return attrs

class QuizQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = '__all__'

class QuizInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizInstance
        fields = '__all__'