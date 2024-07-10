# importing liabraries
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Choice, Question
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

"""This method will be used to get details of a question

        :param Request request: the request received by view
        :param int question_id: The id used to get question who's details will be returned by view

        :returns: response using render method

        :rtype: int
    """
# Creating views
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""This method will be used for Voting for a question in the webapp

        :param request: A client-to-server HTTP request is represented by the `request` parameter in the `vote` function.
        :param int question_id: identify the specific question for which a user is submitting a vote
        
        :returns: response redirect to the 'polls:results

        :rtype: int
    """
    
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
            
            
            
            
"""
    The function retrieves the latest five poll questions and renders them in a template for display.
    
    :param request: represents an HTTP request that is sent to the server.
    
    :return: returning a rendered HTML template named "poll.html" 
    """
@login_required
# function for poll questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


"""
    The method will be used to retrieve a specific question object and renders a results template with the question data.
    
    :param request:  represents an HTTP request that is sent to the server. 
    
    :param question_id: is used to identify the specific question for which the results are being displayed. 

    :return: returns a rendered HTML template `results.html` 
    """
# function for reults
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
