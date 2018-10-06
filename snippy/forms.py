from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from oncotator.models import CSVFile

class SignupForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class FileForm(forms.ModelForm):

    class Meta:
        model = CSVFile
        fields = ('title',)
