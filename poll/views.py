from django.shortcuts import render,redirect
from .forms import CreateForm
from django.contrib import messages
from .models import Polls
from django.http import HttpResponse


def index(Request):
    return render(Request,"base.html")

def create_poll(Request):
    context={}
    form=CreateForm()
    if Request.method=="GET":
        context["form"]=form
        return render(Request,"create_poll.html",context)
    elif Request.method=="POST":
        form=CreateForm(Request.POST)
        if form.is_valid():
            form.save()
            messages.success(Request,"Form Created Successfully")
            context["form"]=form
            return render(Request,"create_poll.html",context)
    return render(Request,"base.html")

def list_questions(request):
    ques=Polls.objects.all()
    context={}
    context["poll_questions"]=ques
    return render(request,"ques_list.html",context)


def vote(request, id):
    poll = Polls.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1

        poll.save()

    context["poll"]=poll
    return render(request, 'vote.html', context)

def poll_result(request,id):
        poll = Polls.objects.get(id=id)
        context = {"poll":poll}
        return render(request, 'poll_result.html', context)