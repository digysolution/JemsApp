from django.contrib import admin
from .models import Utilisateur
from .models import Question
from .models import Epreuve
from .models import Question_Epreuve

admin.site.register(Utilisateur)
admin.site.register(Question)
admin.site.register(Epreuve)
admin.site.register(Question_Epreuve)
