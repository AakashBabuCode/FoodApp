# voting/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Voter
from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['full_name', 'position', 'bio', 'profile_picture']

        
class VoterRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Voter
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            voter = Voter.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
            return voter
        return user
