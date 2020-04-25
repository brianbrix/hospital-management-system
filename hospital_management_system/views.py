from _md5 import md5

from django.shortcuts import render
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from . import models
from django.template import RequestContext
# Create your views here.
from django.urls import reverse
from .forms import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def user_login(request):
    template = loader.get_template('hms/dashboard.html')
    context = {}
    # if request.session.get('username') != "":
    #     return HttpResponse(template.render(context={'session': request.session.get('username')}))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['user_password']
            post = models.Users.objects.filter(email=username, password=password)
            if post:
                request.session['username'] = username
                return HttpResponse(template.render(context, request))
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return render(request, 'hms/user-login.html', {})
    else:
        form=LoginForm()

    return render(request, 'hms/user-login.html', {'form': form})


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def admin_login(request):
    template = loader.get_template('hms/admin/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def doctor_login(request):
    template = loader.get_template('hms/doctor/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))


def user_details(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
