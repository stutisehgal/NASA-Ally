from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.forms.utils import ValidationError
from sitepages.models import (User,Individual)


class CorporateSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username','email','password1','password2')
        model = User

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Company Email Address'

    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_corporate = True
        if commit:
            user.save()

        return user




class IndividualSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username','email','password1','password2')
        model= User


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_individual = True
        user.save()
        individual = Individual.objects.create(user=user)

        return user



class CardInfoForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = ['first_name','last_name','bio','image','instagram_link','linkedin_link','skills','education','work_exp']
