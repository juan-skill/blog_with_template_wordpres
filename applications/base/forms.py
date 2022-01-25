from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('status',)

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                }
            ),
            'last_name':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                }
            ),
            'subject':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el asunto',
                }
            ),
            'message':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese su mensaje',
                }
            ),
        }