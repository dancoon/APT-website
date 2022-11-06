from django import forms
from .models import Member

class ContactForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    # email = forms.CharField()
    # message = forms.Textarea()
    # message = forms.Textarea()

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("fname", "lname", "email", "bio", "position", "is_active")
