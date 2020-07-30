from django import forms
from rekruter.models import User
from django.contrib.auth.forms import UserCreationForm
from meetap.core.snippets import gen_login
from meetap.core.classes import checkifnull as cn
import datetime


class ExtendedCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)
    gender = forms.CharField(widget=forms.HiddenInput(), required=False)
    age = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
            'first_name',
            'gender',
            'age',
        )

    def save(self, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.gender = int(self.cleaned_data["gender"])
        user.age = self.cleaned_data["age"]
        user.mnemo_login = gen_login()

        if commit:
            user.save()
        return user
