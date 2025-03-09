from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import models 

from .models import StudentUser

class SignUpForm(UserCreationForm):
    student_id = forms.CharField(max_length=10, help_text="Student ID must be unique.")
    
    class Meta:
        model = StudentUser
        fields = ['username', 'student_id', 'password1', 'password2']



class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','section']
class IssuedBookForm(forms.Form):
    book=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    studentname=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')