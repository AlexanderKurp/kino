from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Ticket

class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AuthenticationUser(AuthenticationForm):
    pass

class TicketBooking(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['session', 'seat']