from django.shortcuts import render
from .models import QuizStatement, QuizQuestions, QuizInstance
from rest_framework.viewsets import  ModelViewSet
from .serializers import QuizSerializer, QuizQuestionsSerializer, QuizInstanceSerializer
# Create your views here.
from rest_framework.decorators import action


class QuizViewSet(ModelViewSet):
    queryset = QuizStatement.objects.all()
    serializer_class = QuizSerializer

    @action(methods=['post'], detail=True)
    def get_questions(self, request, pk=None):
        quiz = self.get_object()
        questions = quiz.questions.all()  # Assuming 'questions' is the related_name for QuizQuestions in QuizStatement model
        serializer = QuizQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class QuizInstanceViewSet(ModelViewSet):
    queryset = QuizInstance.objects.all()
    serializer_class = QuizInstanceSerializer

    @action(methods=['post'], detail=False)
    def create_quiz_instance(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def get_user_quiz_instances(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_quiz_instances = QuizInstance.objects.filter(user_id=user_id)
        except QuizInstance.DoesNotExist:
            return Response({'error': 'User does not exist or has no quiz instances'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuizInstanceSerializer(user_quiz_instances, many=True)
        return Response(serializer.data)



    
