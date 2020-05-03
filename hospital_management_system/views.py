from _md5 import md5

from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import render
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token

from . import models
from django.template import RequestContext
# Create your views here.
from django.urls import reverse
from .forms import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def user_register(request):
    context = request.POST
    registered = False
    if request.method == 'POST':
        print(
            "Register_registerRegister_registerRegister_registerRegister_registerRegister_registerRegister_registerRegister_register")
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                user.set_password(form.cleaned_data['password'])
                user.save()
                registered = True
                return render(request, 'index', {})
            except IntegrityError as e:
                user.delete()
                return HttpResponse(e)
        else:
            print("Bad form")

        # template = loader.get_template('hms/user-register.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'hms/user-register.html', {'form': form})


@csrf_exempt
def user_login(request):
    template = loader.get_template('hms/dashboard.html')
    context = {}
    # context.update(csrf(request))
    # if request.session.get('username') != "":
    #     return HttpResponse(template.render(context={'session': request.session.get('username')}))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['user_password']
            # post = models.Users.objects.filter(email=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            print("user", user)
            # if post:
            #     request.session['username'] = username
            #     return HttpResponse(template.render(context, request))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    return HttpResponse(template.render(context, request))
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                # return HttpResponseRedirect(reverse('user_login', args=()))
                return render(request, 'hms/user-login.html', {'form': form})

    else:
        form = LoginForm()
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
