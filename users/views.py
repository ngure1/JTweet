from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
def signUpView(request):
  form = CustomUserCreationForm()
  if request.method == "POST":
    user = CustomUserCreationForm(request.POST)
    if user.is_valid():
      user.save()
      return redirect("home")
    else:
      form = user
  context = {"form":form}
  return render(request,'users/signUp.html',context)



def loginView(request):
  context={}
  return render(request,'users/login.html')



def homeView(request):
  return render(request,'users/home.html')