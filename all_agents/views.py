from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse

# Create your views here.

def my_view(request):
    user_agent = get_user_agent(request)
    return HttpResponse(user_agent)
