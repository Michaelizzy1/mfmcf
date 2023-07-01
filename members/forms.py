from .models import *
from django import forms


class MemberForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
        }
    ))

    department = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
        }
    ))

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleFormControlInput1',
        }
    ))

    level = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'inputGroupSelect01',
            'class': 'form-select',
        }
    ))

    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%d%m%Y', attrs={'class': 'form-control', 'type': 'date'}),
    )

    class Meta:
        model = Member
        # widgets = {'date_of_birth': forms.DateInput()}
        fields = '__all__'
