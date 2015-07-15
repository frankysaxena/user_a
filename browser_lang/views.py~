from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse


def get_browser_language(request):
        browser_language_code = request.META.get('HTTP_ACCEPT_LANGUAGE', request)
	return HttpResponse(browser_language_code)

