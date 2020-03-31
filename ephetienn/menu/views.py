from .db_param import insertEvent, supEventDb
from .db_param import insertInscription, deleteMembre, updateMembre
from.db_param import afficherInfoDb, selectUser, modifMembreDb, updateUser, selectMembre
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .envoiemail import envoi, envoiCopie, confirmInscription
from . import forms



def home(request):
    return render(request, 'menu/acceuil.html')



def inscription(request):

    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = forms.formInscription(request.POST or None)
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
        confirmInscription(emailParents, nom, prenom)

        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.

    return render(request, 'menu/inscription.html', locals())

def event(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = forms.formEvent(request.POST or None)
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


        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'menu/insertEvent.html', locals())


def emailView(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            renvoi = form.cleaned_data['renvoi']
            print(renvoi)
            if renvoi:
                envoiCopie(from_email, subject, message)
            try:
                envoi(from_email, subject, message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "menu/contact.html", locals())

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def admin(request):

    form = forms.connexion(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        user = form.cleaned_data['user']
        mdp = form.cleaned_data['mdp']
        redirect = selectUser(user, mdp)
        print(redirect)

        envoi = True

        if redirect == True:
            return render(request, 'menu/admin.html', locals())

        else :
            return render(request, 'menu/acceuil.html', locals())

    return render(request, 'menu/acceuil.html', locals())

def supEvent(request):
    form = forms.formSupEvent(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        nom = form.cleaned_data['nom']
        date = form.cleaned_data['date']

        supEventDb(nom, date)

        envoi = True

    return render(request, "menu/supEvent.html", locals())

def supMembre(request):
    form = forms.modifierMembre(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        id = form.cleaned_data['id']


        deleteMembre(id)

        envoi = True

    return render(request, "menu/supMembre.html", locals())

def affMembre(request):

    afficher = affichageMembres()


    return render(request, "menu/membre.html", locals())

def modifMembre(request):

    answer=[]
    form = forms.modifierMembre(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        id = form.cleaned_data['id']
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        dateNaiss = form.cleaned_data['dateNaiss']
        numeroTel = form.cleaned_data['numeroTel']
        emailParents = form.cleaned_data['emailParents']
        remarques = form.cleaned_data['remarques']

        answer = selectMembre(id)
        print("answer: ", answer)
        updateMembre(id, nom, prenom, dateNaiss, numeroTel, emailParents, remarques)
        envoi = True

    afficher = answer


    return render(request, "menu/modifierMembre.html", locals())

def affichageMembres():
    liste = []
    afficher= " "



    membres = afficherInfoDb('membre')
    print(type(membres))
    print(membres)

    i = 0
    while i < len(membres):
        print(membres[i][0])
        liste += [[membres[i][0], membres[i][1], membres[i][2]]]
        i += 1

    print(liste)
    print(type(liste))

    print("résultat désirer: ")
    for id, nom, prenom in liste:
        print("id: {} nom: {} prenom : {}".format(id, nom, prenom))
        afficher += ("id: {} nom: {} prenom : {} \n ".format(id, nom, prenom))
        print("test: ", afficher)



    return liste

def affichageEvent():

    #Print utiliser pour debug
    eventAvenir = []
    afficher = " "

    events = afficherInfoDb('event')
    print(type(events))
    print(events)

    i = 0
    while i < len(events):
        print(events[i][0])
        eventAvenir += [[events[i][0], events[i][1], events[i][2]]]
        i += 1

    print("eventAvenir:", eventAvenir)
    print(type(eventAvenir))


    print("résultat désirer: ")
    for nom, date, description in eventAvenir:
        afficher += ("nom: {} date: {} description : {} \n".format(nom, date, description))
        print("test: ", afficher)

    return eventAvenir

def affEvent(request):

    eventAvenir = affichageEvent()

    return render(request, "menu/affEvent.html", locals())

