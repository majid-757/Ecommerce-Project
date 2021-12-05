from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 


from .models import Profile
from .forms import ProfileForm, SignUpForm





def sign_up(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(''))


    context = {
        'form': form,

    }

    return render(request, 'App_Login\sign_up.html', context)














