from django import forms


class formInscription(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    dateNaiss = forms.DateField(label="format 2020-03-21")
    numeroTel = forms.CharField(label="numer telephone")
    emailParents = forms.EmailField(label="Votre adresse e-mail")
    remarques = forms.CharField(max_length=1000)


class formEvent(forms.Form):
    date = forms.DateField(label="date de l'évenement")
    nom = forms.CharField(max_length=45)
    description = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
