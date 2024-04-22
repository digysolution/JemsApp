from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo_profil = models.ImageField(upload_to='images', blank=True, null=True)
    date_inscription = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField('auth.Group', related_name='utilisateurs')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='utilisateurs')

class Question(models.Model):
    texte_question = models.TextField()
    options = models.JSONField()
    reponse_correcte = models.TextField()
    difficulte = models.IntegerField()
    theme = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Epreuve(models.Model):
    titre = models.CharField(max_length=100)
    date_creation = models.DateField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Question_Epreuve(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)