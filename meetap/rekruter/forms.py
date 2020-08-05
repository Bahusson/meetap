from django import forms
from rekruter.models import User
from django.contrib.auth.forms import UserCreationForm
from meetap.core.snippets import gen_login, calculateAge as ca
import datetime


class ExtendedCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)
    gender = forms.CharField(widget=forms.HiddenInput(), required=False)
    age = forms.DateField(input_formats=['%Y-%m-%d'])

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
        user.date_joined = datetime.datetime.now()
        userage = ca(user.age)
        if userage >= 18:
            user.is_adult = 2
        elif userage >= 15:
            user.is_adult = 1
        else:
            user.is_adult = 0

        if commit:
            user.save()
        return user
