from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers une autre page après la connexion réussie
            return redirect('home')
        else:
            # Gérer le cas où l'authentification échoue
            return render(request, 'connexion.html', {'erreur': True})
    else:
        return render(request, 'connexion.html')