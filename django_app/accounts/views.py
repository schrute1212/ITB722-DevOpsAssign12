from django.shortcuts import render, redirect
from .models import Login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        if username and password:
            if not Login.objects.filter(username=username).exists():
                Login.objects.create(username=username, password=password)
                return redirect("login")
            else:
                messages.error(request, "User already exists")
        else:
            messages.error(request, "Please enter both fields")
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        try:
            user = Login.objects.get(username=username, password=password)
            request.session["username"] = user.username
            return redirect("home")
        except Login.DoesNotExist:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")

def home(request):
    username = request.session.get("username")
    if not username:
        return redirect("login")
    return render(request, "home.html", {"username": username})

def logout_view(request):
    request.session.flush()
    return redirect("login")
