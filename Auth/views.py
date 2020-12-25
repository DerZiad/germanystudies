from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .models import Personne

import hashlib
import Auth.ValidEntry.ValidatorInscript as validator
import Auth.ValidEntry.utilconverter as Converter
import json
from django.core import serializers
# Create your views here.

def index(request):
    template = loader.get_template("session/session.html")
    return HttpResponse(template.render(request = request))


def inscription(request):
    if(request.method == 'GET'):
        test = Converter.testerSession(request)
        if test == False:
            template = loader.get_template("login/signup.html")
            return HttpResponse(template.render(request = request))
        else:
            return HttpResponseRedirect("/")
    else:
        id = request.POST.get('id')
        if id=="1":
            firstpane = validator.checkFirstPanelInBase(request)
            return JsonResponse(firstpane)
        elif id=="2":
            secondpane = validator.checkSecondPaneInBase(request)
            return JsonResponse(secondpane)
        else:
            attiribut = request.POST
            nom = attiribut['nom']
            prenom = attiribut['prenom']
            birthday = attiribut['datedenaissance']
            username = attiribut['username']
            password = attiribut['password']
            email = attiribut['email']
            telephone = attiribut['telephone']
            cpassword = hashlib.md5(password.encode())
            personne = Personne(nom=nom,prenom=prenom,datedenaissance=birthday,username=username,password = cpassword.hexdigest(),
                email = email,telephone = telephone)
            personne.save()
            #return HttpResponse("<h1>Good</h1>")
            Converter.converttodata(request,personne)
            return HttpResponseRedirect("/")
def seconnecter(request):
    if(request.method == 'POST'):
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = hashlib.md5(password.encode())
        users = Personne.objects.filter(email = username,password = cpassword)
        if len(users) != 0:
            Converter.converttodata(request,users[0])
            return HttpResponseRedirect("/")
        else:
            test = Converter.testerSession(request)
            if test == True:
                return HttpResponseRedirect("/")
            else:
                template = loader.get_template("login/signin.html")
                erreurs = {"erreur":"Username ou mot de passe est non valide"}
                return render(request,"login/signin.html",erreurs)
    else:
        template = loader.get_template("login/signin.html")
        return HttpResponse(template.render(request= request))
def disconnect(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect("/")
