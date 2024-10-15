from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from app.forms import AddEventForm
from django.contrib.auth import login, authenticate
from django.shortcuts import  redirect

def index(request):
    html = render(request, "app/index.html")
    return HttpResponse(html)


@login_required
def login_test(request):
    return render(request, "app/index.html")



def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Created new event")

    return HttpResponseRedirect(reverse('index'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})