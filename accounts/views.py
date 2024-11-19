from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages

# -------------------------------- Home View --------------------------------
def home(request):
    return render(request, 'index.html')
# -------------------------------- Login View --------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')
# -------------------------------- Logout View --------------------------------
def logout_view(request):
    logout(request)
    return redirect('home')
# -------------------------------- Singup View --------------------------------
def singup_view(request):
    return render(request, 'singup.html')
