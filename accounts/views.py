from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()


    return render(request, 'register.html', {'form':form})
