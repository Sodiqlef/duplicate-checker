from django import forms
from main.models import Duplicates


class DuplicateForm(forms.ModelForm):
    duplicate = forms.CharField(max_length=100000, widget=forms.Textarea(
        attrs={'rows':10, 'cols':15, 'placeholder': 'https.......'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


    class Meta:
        model = Duplicates
        fields = ['duplicate']