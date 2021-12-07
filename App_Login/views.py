from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 
# Messages
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm, SignUpForm





def sign_up(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
            return HttpResponseRedirect(reverse('App_Login:login'))


    context = {
        'form': form,

    }

    return render(request, 'App_Login/sign_up.html', context)




def login_user(request):
    form  = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return HttpResponse('Logged In')

    context = {
        'form': form,
    }

    return render(request, 'App_Login/login.html', context)



@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, 'You are logged out')

    return HttpResponse('Logged Out')




@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')

            form = ProfileForm(instance=profile)


    context = {
        'form': form,
    }

    return render(request, 'App_Login/change_profile.html', context)





def change_profile(request):
    pass
















