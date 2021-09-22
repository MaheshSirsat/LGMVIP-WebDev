from django.forms import fields
from SRMS import models
from django import forms
from . import models

class StudentInfo(forms.ModelForm):
    
    class Meta():
        model=models.StudentInfo
        fields=("__all__")
class result(forms.Form):
    PRN_No=forms.CharField(label="Enter your PRN No",max_length=20)
    Mother=forms.CharField(max_length=30,label="Mother Name")
from django.contrib.auth.models import User
from django.forms import fields
 
class SignUp(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name']