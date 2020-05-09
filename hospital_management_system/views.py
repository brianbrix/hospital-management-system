from _md5 import md5

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from werkzeug import Response

from . import models
from django.template import RequestContext
# Create your views here.
from django.urls import reverse
from .forms import *
from rest_framework import viewsets, status
from .serializers import *
import requests
from .models import Users


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_email')
    serializer_class = UserSerializer


class UserJSONRenderer(object):
    pass


class UserRegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = UserRegistrationSerializer
    queryset = Users.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@api_view(['GET', 'POST'])
def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        serialized = UserRegistrationSerializer(data=request.data)
        if serialized.is_valid():
            user = form.save(commit=False)
            try:
                user_email = form.cleaned_data['user_email']
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                address = form.cleaned_data['address']
                city = form.cleaned_data['city']
                password = form.cleaned_data['password']
                gender = form.cleaned_data['gender']
                data = {
                    "user_email": user_email,
                    "firstname": firstname,
                    "lastname": lastname,
                    "address": address,
                    "city": city,
                    "password": password
                }
                if serialized.create(data):
                    messages.info(request, 'Your registration was completed successfully!')
                    return redirect('user_login')
                else:
                    messages.warning(request, 'Failed to register! Please try again later.')
                    return redirect('user_register')
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['user_password']
            user = authenticate(username=username, password=password)
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
    template = loader.get_template('hms/dashboard.html')
    context = {}
    if request.method == 'POST':
        form = DocLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['doc_username']
            password = form.cleaned_data['doctor_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    return HttpResponse(template.render(context, request))
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                # return HttpResponseRedirect(reverse('user_login', args=()))
                return render(request, 'hms/doctor/index.html', {'form': form})

    else:
        form = DocLoginForm()
    return render(request, 'hms/doctor/index.html', {'form': form})


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
