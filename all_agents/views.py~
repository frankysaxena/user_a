from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse



def my_view(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponse(user_agent)
    elif user_agent.is_tablet:
       return HttpResponse(user_agent)
    elif user_agent.is_touch_capable:
	return HttpResponse(user_agent)	
    elif user_agent.is_pc:
	return HttpResponse(user_agent)
    elif user_agent.is_bot:
	return HttpResponse(user_agent)

