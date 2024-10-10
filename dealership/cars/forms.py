from django import forms
from .models import Car, Comment


class NewCar(forms.ModelForm):
    make = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Марка'}))
    model = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Модель'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Год'}), required=False)
    description = forms.TextInput()

    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description',)

class NewComment(forms.ModelForm):
    text = forms.TextInput()
    class Meta:
        model = Comment
        fields = ('content',)
