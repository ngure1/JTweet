from django.shortcuts import render

def signUpView(request):
  context={}
  return render(request,'users/signUp.html')


def loginView(request):
  context={}
  return render(request,'users/login.html')