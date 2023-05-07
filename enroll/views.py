from django.shortcuts import render
from . forms import UserForm
from . models import User
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
           reg = User(
               name=form.cleaned_data["name"], 
               department=form.cleaned_data["department"], 
               semester=form.cleaned_data["semester"])
           reg.save()
    else:
        form = UserForm()
    return render(request, "enroll/register.html", {"form": form})
