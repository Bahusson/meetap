from django import forms
from rekruter.models import User
# import datetime


# Zmienia ustawienia profilu użytkownika.
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    avatar1 = forms.ImageField(required=False)
    avatar2 = forms.ImageField(required=False)
    avatar3 = forms.ImageField(required=False)
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
         'first_name', 'avatar1', 'avatar2', 'avatar3', 'gender', 'age',
         'sex_preference', 'sex_role_activity', 'sex_role_dominance',
         'alcohol', 'tobacco', 'other_drugs', 'about_me', 'interests',
         'showme_adultcontent', 'showmy_sexorientation', 'showmy_sexrole',
         'showme_commercial', 'showme_massevents', 'sendme_inv_status_me',
         'sendme_inv_status_others', 'sendme_invitations',
         'sendme_friend_events', 'sendme_join_request'
         )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.avatar1 = self.cleaned_data["avatar1"]
        user.avatar2 = self.cleaned_data["avatar1"]
        user.avatar3 = self.cleaned_data["avatar1"]
        user.gender = self.cleaned_data["gender"]
        user.age = self.cleaned_data["age"]
        user.sex_preference = self.cleaned_data['sex_preference']
        user.sex_role_activity = self.cleaned_data['sex_role_activity']
        user.sex_role_dominance = self.cleaned_data['sex_role_dominance']
        user.alcohol = self.cleaned_data['alcohol']
        user.tobacco = self.cleaned_data['tobacco']
        user.other_drugs = self.cleaned_data['other_drugs']
        user.telephone = self.cleaned_data['telephone']
        user.other_contact = self.cleaned_data['other_contact']
        user.about_me = self.cleaned_data['about_me']
        user.interests = self.cleaned_data['interests']
        user.showme_adultcontent = self.cleaned_data['showme_adultcontent']
        user.showmy_sexorientation = self.cleaned_data['showmy_sexorientation']
        user.showmy_sexrole = self.cleaned_data['showmy_sexrole']
        user.showme_commercial = self.cleaned_data['showme_commercial']
        user.showme_massevents = self.cleaned_data['showme_massevents']
        user.sendme_inv_status_me = self.cleaned_data['sendme_inv_status_me']
        user.sendme_inv_status_others = self.cleaned_data['sendme_inv_status_others']
        user.sendme_invitations = self.cleaned_data['sendme_invitations']
        user.sendme_friend_events = self.cleaned_data['sendme_friend_events']
        user.sendme_join_request = self.cleaned_data['sendme_join_request']

        if commit:
            user.save()
        return user
