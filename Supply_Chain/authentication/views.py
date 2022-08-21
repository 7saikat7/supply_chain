from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from authentication.forms import CustomRegisterForm

UserModel = get_user_model()

def RegisterForm(request):
    form = CustomRegisterForm()
    
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponse("Success")
            #  return redirect('')

    context = {'form':form}
    return render(request, 'authentication/Register.html', context)

def LoginForm(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse("Success")
            # return redirect()
    else:
        form = AuthenticationForm(request)

    context = {'form':form}
    return render(request, 'authentication/Login.html', context)
