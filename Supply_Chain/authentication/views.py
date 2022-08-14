from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserModel.objects.get(email=email)
        except:
            messages.error(request, 'User not found')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Success")
            #  return redirect('')

    return render(request, 'authentication/Login.html')
