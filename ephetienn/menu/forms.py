from django import forms

class formInscription(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    dateNaiss = forms.DateField(label="format 2020-03-21")
    numeroTel = forms.CharField(label="numer telephone")
    emailParents = forms.EmailField(label="Votre adresse e-mail")
    remarques = forms.CharField(max_length=1000)

class formEvent(forms.Form):
    date = forms.DateField(label="date de l'évenemnt'")
    nom = forms.CharField(max_length=45)
    description = forms.CharField(max_length=1000)

