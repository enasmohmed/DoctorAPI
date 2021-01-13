from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import UserRegisterForm

# Create your views here.



# Function Register

def signup_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect('home')
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "registration/signup.html", context)




