# importing liabraries
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Choice, Question
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Creating views
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# function for voting 
def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(
            pk=request.POST['choice']
            )
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form
            return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # user hits the Back button.
            return HttpResponseRedirect( reverse('polls:results', args=(question_id,))
            )
            
@login_required
# function for poll questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

# function for reults
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

