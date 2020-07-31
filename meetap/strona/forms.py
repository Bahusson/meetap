from django import forms
from rekruter.models import User
#import datetime


# Zmienia ustawienia profilu użytkownika.
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    avatar = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.HiddenInput(), required=False)
    age = forms.DateField(input_formats=['%d.%m.%Y'])
    sex_preference = forms.CharField(widget=forms.HiddenInput(), required=False)
    sex_role_activity = forms.CharField(widget=forms.HiddenInput(), required=False)
    sex_role_dominance = forms.CharField(widget=forms.HiddenInput(), required=False)
    alcohol = forms.CharField(widget=forms.HiddenInput(), required=False)
    tobacco = forms.CharField(widget=forms.HiddenInput(), required=False)
    other_drugs = forms.CharField(max_length=300, required=False)
    telephone = forms.CharField(max_length=30, required=False)
    other_contact = forms.CharField(max_length=300, required=False)
    about_me = forms.CharField(max_length=1500, required=False)
    interests = forms.CharField(max_length=500, required=False)
    showme_adultcontent = forms.BooleanField(required=False)
    showmy_sexorientation = forms.BooleanField(required=False)
    showmy_sexrole = forms.BooleanField(required=False)
    showme_commercial = forms.BooleanField(required=True)
    showme_massevents = forms.BooleanField(required=True)
    sendme_inv_status_me = forms.BooleanField(required=True)
    sendme_inv_status_others = forms.BooleanField(required=True)
    sendme_invitations = forms.BooleanField(required=True)
    sendme_friend_events = forms.BooleanField(required=True)
    sendme_join_request = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = (
         'first_name', 'avatar', 'gender', 'age', 'sex_preference',
         'sex_role_activity', 'sex_role_dominance', 'alcohol', 'tobacco',
         'other_drugs', 'about_me', 'interests', 'showme_adultcontent',
         'showmy_sexorientation', 'showmy_sexrole', 'showme_commercial',
         'showme_massevents', 'sendme_inv_status_me', 'sendme_inv_status_others',
         'sendme_invitations', 'sendme_friend_events', 'sendme_join_request'
         )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.avatar = self.cleaned_data["avatar"]
        
        if commit:
            user.save()
        return user
