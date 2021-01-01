from django.contrib import admin
from Auth.models import Personne, Professeur
from Grammar.models import Ubung, Essai
from Lesen.models import Text, Fragen, Answers

admin.site.register(Answers)
admin.site.register(Text)
admin.site.register(Fragen)
admin.site.register(Personne)
admin.site.register(Professeur)
admin.site.register(Ubung)
admin.site.register(Essai)
