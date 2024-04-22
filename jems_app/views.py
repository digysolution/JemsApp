from django.shortcuts import render, redirect
from .forms import InscriptionForm

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirection vers la page d'accueil après l'inscription
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})
