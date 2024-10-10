from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': 'Придумайте себе имя',
            })
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Ваш email',
            })
        self.fields['password1'].widget.attrs\
            .update({
                'placeholder': 'Придумайте пароль',
            })
        self.fields['password2'].widget.attrs\
            .update({
                'placeholder': 'Повторите пароль',
            })
        
        