from django import forms
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nom de l'utilisateur"
        self.fields['email'].label = "Adresse email"
        self.fields['telephone'].label = "Téléphone"
        self.fields['photo_profil'].label = "Photo de profil"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmer le mot de passe"
        
        # Personnaliser les messages d'aide pour chaque champ
        self.fields['username'].help_text = "Saisissez votre nom d'utilisateur."
        self.fields['email'].help_text = "Saisissez votre adresse email."
        self.fields['telephone'].help_text = "Saisissez votre numéro de téléphone (facultatif)."
        self.fields['photo_profil'].help_text = "Téléchargez votre photo de profil (facultatif)."
        self.fields['password1'].help_text = "Votre mot de passe doit contenir au moins 8 caractères."
        self.fields['password2'].help_text = "Confirmez votre mot de passe."
        
        # Personnaliser les messages d'erreur pour chaque champ
        self.fields['username'].error_messages = {'required': 'Ce champ est obligatoire.'}
        self.fields['email'].error_messages = {'required': 'Ce champ est obligatoire.'}
        self.fields['password1'].error_messages = {'required': 'Ce champ est obligatoire.'}
        self.fields['password2'].error_messages = {'required': 'Ce champ est obligatoire.'}

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'telephone', 'photo_profil')