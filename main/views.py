from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem

def index(request):
    problemList = Problem.objects.all().order_by('-id')
    data = {'problemList': problemList}
    return render(request,'main/index.html', data)

def board(request, id):
    problem = get_object_or_404(Problem, pk=id)
    return render(request, 'main/board.html', {'problem': problem})

def result(request, id):
    answer = request.POST['radio']
    id = get_object_or_404(Problem, pk=id)
    result = 0
    if int(id.answer_number) == int(answer):
        result = 1
        id.success += 1
    else:
        id.fail += 1
    id.save()
    return render(request, 'main/result.html', {'result' : result})

def boardForm(request):
    return render(request, 'main/boardForm.html')

def add(request):
    problem = Problem()
    title = request.POST['title']
    quiz1 = request.POST['quiz1']
    quiz2 = request.POST['quiz2']
    quiz3 = request.POST['quiz3']
    quiz4 = request.POST['quiz4']
    answer = request.POST['answer']

    problem.title = title;
    problem.question1 = quiz1;
    problem.question2 = quiz2;
    problem.question3 = quiz3;
    problem.question4 = quiz4;
    problem.answer_number = answer;
    problem.success = 0;
    problem.fail = 0;
    problem.save()

    return HttpResponseRedirect('/')