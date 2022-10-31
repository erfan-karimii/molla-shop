from django import forms
from .models import KhabarName , ContactUs, ContactDetail ,OurShop

class KhabarNameForm(forms.Form):
    email = forms.EmailField()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if KhabarName.objects.filter(email=email).exists():
            raise  forms.ValidationError('duplicate email')
        return email

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','phone','title','body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','readonly ':'true'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','readonly ':'true'}),
            'title': forms.TextInput(attrs={'class': 'form-control','readonly ':'true'}),
            'body': forms.Textarea(attrs={'class': 'form-control','readonly ':'true'}),
        }
        
class OurShopForm(forms.ModelForm):
    class Meta:
        model = OurShop
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'work_days': forms.TextInput(attrs={'class': 'form-control'}),
            'work_time': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContactUsDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'work_days': forms.TextInput(attrs={'class': 'form-control'}),
            'work_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
