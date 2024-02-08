from django import forms
from .models import *


# class FanForm(forms.Form):
#     nomi=forms.CharField(max_length=30,label="Fan nomi"),
#     oqituvchi=forms.CharField(max_length=30,label="O'qituvchi")
#     credit=forms.IntegerField(min_value=0,label="Necha credit: "),


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'


class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = '__all__'


class KursForm(forms.ModelForm):
    class Meta:
        model = Kurs
        fields = '__all__'
