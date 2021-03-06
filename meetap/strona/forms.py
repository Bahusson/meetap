from django import forms
from rekruter.models import User
from meetap.core.classes import checkifnull as cn
from meetap.core.snippets import calculateAge as ca, flare


# Zmienia ustawienia profilu użytkownika.
# Avatar 2 i 3 do wyrzucenia na dodatkowe formularze,
# bo nie da się zrobić więcej niż 1 na formularz. :/
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    avatar1 = forms.ImageField(required=False)
    # avatar2 = forms.ImageField(required=False)
    # avatar3 = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.HiddenInput(), required=False)
    age = forms.DateField(input_formats=['%d.%m.%Y'])
    telephone = forms.CharField(max_length=30, required=False)
    other_contact = forms.CharField(max_length=300, required=False)
    sex_preference = forms.CharField(
     widget=forms.HiddenInput(), required=False)
    other_preference = forms.CharField(max_length=30, required=False)
    sex_role_activity = forms.CharField(
     widget=forms.HiddenInput(), required=False)
    sex_role_dominance = forms.CharField(
     widget=forms.HiddenInput(), required=False)
    alcohol = forms.CharField(widget=forms.HiddenInput(), required=False)
    tobacco = forms.CharField(widget=forms.HiddenInput(), required=False)
    other_drugs = forms.CharField(max_length=300, required=False)
    about_me = forms.CharField(max_length=1500, required=False)
    interests = forms.CharField(max_length=500, required=False)
    showme_adultcontent = forms.BooleanField(required=False)
    showmy_sexorientation = forms.BooleanField(required=False)
    showmy_sexrole = forms.BooleanField(required=False)
    showme_sexevents = forms.BooleanField(required=False)
    showme_commercial = forms.BooleanField(required=False)
    showme_massevents = forms.BooleanField(required=False)
    sendme_inv_status_me = forms.BooleanField(required=False)
    sendme_inv_status_others = forms.BooleanField(required=False)
    sendme_invitations = forms.BooleanField(required=False)
    sendme_friend_events = forms.BooleanField(required=False)
    sendme_join_request = forms.BooleanField(required=False)
    delete_image = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
         'first_name', 'avatar1',  # 'avatar2', 'avatar3',
         'gender', 'age',  'telephone', 'other_contact',
         'sex_preference', 'other_preference', 'sex_role_activity',
         'sex_role_dominance', 'alcohol', 'tobacco', 'other_drugs',
         'about_me', 'interests', 'showme_sexevents',
         'showme_adultcontent', 'showmy_sexorientation', 'showmy_sexrole',
         'showme_commercial', 'showme_massevents', 'sendme_inv_status_me',
         'sendme_inv_status_others', 'sendme_invitations',
         'sendme_friend_events', 'sendme_join_request',
         )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        # user.avatar2 = cn(self.cleaned_data["avatar1"], "")
        # user.avatar3 = cn(self.cleaned_data["avatar1"], "")
        user.gender = cn(self.cleaned_data["gender"], 5)
        user.age = self.cleaned_data["age"]
        user.telephone = self.cleaned_data['telephone']
        user.other_contact = self.cleaned_data['other_contact']
        user.sex_preference = cn(self.cleaned_data['sex_preference'], 0)
        user.other_preference = self.cleaned_data['other_preference']
        user.sex_role_activity = cn(self.cleaned_data['sex_role_activity'], 0)
        user.sex_role_dominance = cn(
         self.cleaned_data['sex_role_dominance'], 0)
        user.alcohol = cn(self.cleaned_data['alcohol'], 0)
        user.tobacco = cn(self.cleaned_data['tobacco'], 0)
        user.other_drugs = cn(self.cleaned_data['other_drugs'], "")
        user.about_me = self.cleaned_data['about_me']
        user.interests = self.cleaned_data['interests']
        user.showme_adultcontent = cn(
         self.cleaned_data['showme_adultcontent'], False)
        user.showmy_sexorientation = cn(
         self.cleaned_data['showmy_sexorientation'], False)
        user.showmy_sexrole = cn(self.cleaned_data['showmy_sexrole'], False)
        user.showme_sexevents = cn(
         self.cleaned_data['showme_sexevents'], False)
        user.showme_commercial = self.cleaned_data['showme_commercial']
        user.showme_massevents = self.cleaned_data['showme_massevents']
        user.sendme_inv_status_me = self.cleaned_data['sendme_inv_status_me']
        user.sendme_inv_status_others = self.cleaned_data['sendme_inv_status_others']
        user.sendme_invitations = self.cleaned_data['sendme_invitations']
        user.sendme_friend_events = self.cleaned_data['sendme_friend_events']
        user.sendme_join_request = self.cleaned_data['sendme_join_request']
        imgdelete = self.cleaned_data["delete_image"]
        if imgdelete is True:
            user.avatar1 = None
        else:
            user.avatar1 = self.cleaned_data["avatar1"]
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
