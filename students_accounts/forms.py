from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from students_accounts.models import Chat, Book
from django import forms




class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'year', 'cover')        


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
