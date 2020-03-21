from django.http import HttpResponse
from django.shortcuts import render
from .db_param import insertEvent
from .forms import formInscription
from .db_param import insertInscription
from .forms import formEvent

def home(request):
    return render(request,'menu/acceuil.html')

def inscription(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = formInscription(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        dateNaiss = form.cleaned_data['dateNaiss']
        numeroTel= form.cleaned_data['numeroTel']
        emailParents = form.cleaned_data['emailParents']
        remarques = form.cleaned_data['remarques']

        #envoie des donnees du formulaire vers la base de données
        insertInscription(nom, prenom, dateNaiss, numeroTel, emailParents, remarques)

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'menu/inscription.html', locals())

def event(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = formEvent(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        date= form.cleaned_data['date']
        nom = form.cleaned_data['nom']
        description = form.cleaned_data['description']

        # envoie des donnees du formulaire vers la base de données
        insertEvent(date, nom, description)

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'menu/insertEvent.html', locals())
