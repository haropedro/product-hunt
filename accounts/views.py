from django.shortcuts import render

def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #todo Need to route to homepage
    # and dont forget to logout :)
    return render(request, 'accounts/signup.html')
