from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    tltle = forms.CharField(max_length=30)
    body = forms.CharField(max_length=1500, required=False)
    image = forms.ImageField(required=False)
    datefrom = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    dateto = forms.DateTimeField(
     input_formats=['%d.%m.%Y %H:%M:%S'], required=False)

    class Meta:
        model = Event
        fields = ('title', 'body', 'image', 'datefrom', 'dateto')

    def save(self, user_id, commit=True):
        event = (EventForm, self).save(commit=False)
        event.title = self.cleaned_data["title"]
        event.body = self.cleaned_data["body"]
        event.image = self.cleaned_data["image"]
        event.datefrom = self.cleaned_data["datefrom"]
        event.dateto = self.cleaned_data["dateto"]
        event.owner = user_id
        if commit:
            event.save()
        return event
