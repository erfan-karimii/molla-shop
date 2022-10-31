from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            # 'is_active':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'is_staff':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'token':forms.TextInput(attrs={'class': 'form-control'}),
            'is_verify':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password':forms.TextInput(attrs={'class': 'form-control'})
        }


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"لطفا یک رمز امن بگذارید"}))