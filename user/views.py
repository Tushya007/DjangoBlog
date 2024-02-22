from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def user_registration_form(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        form = UserRegisterForm()
        return redirect("{% url 'login' %}")
    context = {
        "form":form
    }
    return render(request,'users/user_register.html',context)

@login_required(login_url="../login/")
def logoutView(request):
    logout(request)
    return render(request,'users/logout.html')
