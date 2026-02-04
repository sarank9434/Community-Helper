from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedSignupForm(UserCreationForm):
    # Standard User fields we want to make visible/required
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    
    # Custom Profile fields
    address = forms.CharField(max_length=200, required=True)
    contact = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Now update the Profile created by the Signal
            user.profile.address = self.cleaned_data['address']
            user.profile.contact = self.cleaned_data['contact']
            user.profile.save()
        return user