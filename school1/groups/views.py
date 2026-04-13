from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from groups.models import Questions
from groups.models import Tests

from groups.models import Answer,  Choice




#class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        questions = Questions.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)


#class QuestionAnswer(GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    #serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            #return Response({'result': 'OK'})


#class ChoiceSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['pk', 'title', 'points', 'percent', 'lock_other', ]

    def get_percent(self, obj):
        total = Answer.objects.filter(question=obj.question).count()
        current = Answer.objects.filter(question=obj.question, choice=obj).count()
        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)


#class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Questions
        fields = ['pk', 'title', 'choices', 'max_points', ]


#class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()

    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        user = self.context.user
        for question_id, in answers:  # тут наверное лишняя запятая , ошибка в оригинальном коде
            question = Questions.objects.get(pk=question_id)
            choices = answers[question_id]
            for choice_id in choices:
                choice = Choice.objects.get(pk=choice_id)
                Answer(user=user, question=question, choice=choice).save()
                user.is_answer = True
                user.save()

#def questionList(request, question):
    #return render(request,'groups/tests.html',{'question':question})

#def testing(request,test_id):
    question = Questions.objects.filter(test_id=test_id)
    for q in question:
        #return questionList(request,q)
    


#def test(request,test_id):
    #test = Tests.objects.get(pk=test_id)
    #q = Questions.objects.filter(test_id=test_id)
    #paginator = Paginator(q,1)
    #page_num = request.GET.get('page')
    #page_obj = paginator.get_page(page_num)
    #return render(request,'groups/test.html',{'page_obj':page_obj,'test':test})
    


def index(request):
    return render(request, 'groups/index.html')

def about_us_prep(request):
    return render(request, 'groups/about_us_prep.html')

def base_of_knowledge(request):
    return render(request, 'groups/base_of_knowledge.html')

def Courses(request):
    return render(request, 'groups/Courses.html')

def Groups(request):
    return render(request, 'groups/groups.html')

def Help_prep(request):
    return render(request, 'groups/Help_prep.html')

def Lectures(request):
    return render(request, 'groups/Lectures.html')

def material_for_students(request):
    return render(request, 'groups/material_for_students.html')

def profile_prep(request):
    return render(request, 'groups/profile_prep.html')

def results(request):
    return render(request, 'groups/results.html')

#def Tests(request):
    #return render(request, 'groups/Tests.html')