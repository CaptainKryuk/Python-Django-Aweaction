from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegistration, Login
from .models import Profile, User, Projects
from django.contrib.auth.decorators import *
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def accounts(request):
    return render(request, 'accounts.html')


@csrf_protect
def registration(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # When user becomes registered on our site we create blank profile binded with his user model
            profile_form = Profile.objects.create(user=new_user)
            return render(request, 'registration_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'registration.html', {'user_form': user_form})


@csrf_protect
def login(request):
    if request.method == 'POST':
        login_form = Login(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponse("Your account is disabled")
            else:
                return HttpResponse("Your login is invalid")
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})


@login_required()
def dashboard(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        name = request.POST['name']
        description = request.POST['description']
        r = Projects.objects.create(user=request.user, name=name, description=description, document=document)
        r.save()
        return HttpResponseRedirect('/success/')
    return render(request, 'dashboard.html')


@login_required()
def downloading(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        name = request.POST['name']
        description = request.POST['description']
        r = Projects.objects.create(user=request.user, name=name, description=description, document=document)
        r.save()
        return HttpResponseRedirect('/success/')
    return render(request, 'downloading.html')


@login_required()
def edit(request):
    return render(request, 'profile_edit.html')


@login_required()
def edit_additional_info(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        date_of_birth = request.POST['date_of_birth']
        direction = request.POST['direction']
        r = Profile.objects.get(user=request.user)
        r.photo = photo
        r.date_of_birth = date_of_birth
        r.direction = direction
        r.save()
        return HttpResponseRedirect('done/')
    return render(request, 'profile_edit_additional_info.html')


@login_required()
def edit_additional_info_done(request):
    return render(request, 'profile_edited_successfully.html')
