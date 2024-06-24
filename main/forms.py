from django import forms
from django.utils.translation import gettext_lazy as _

class LanguageForm(forms.Form):
    language_choices = [
        ('en', _('English')),
        ('fr', _('French')),
        ('es', _('Spanish')),
        # Ajoutez d'autres langues si nécessaire
    ]
    
    language = forms.ChoiceField(
        choices=language_choices,
        label=_('Select your language'),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
    )
