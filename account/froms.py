from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your username'}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password'}))


class UserRegisterationForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your username'}))
    email=forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'your email'}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password'}))
    password2=forms.CharField(max_length=30,label='verfiy',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'verfiy your password'}))
    phone=forms.CharField(max_length=30,label='phone number',widget=forms.TextInput(attrs={'class':'form-control','placeholder':' your phone number'}))
    

    def clean_password2(self):
        p1=self.cleaned_data['password']
        p2=self.cleaned_data['password2']
        if p1 != p2:
            raise forms.ValidationError('password must match')
        return p1






    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('this email already exist')
        return email


class EditProfileForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Profile
        fields=('bio','age')


class PhoneLoginForm(forms.Form):
    phone=forms.IntegerField()






    def clean_phone(self):
        phone=Profile.objects.filter(phone=self.cleaned_data['phone'] )
        if not phone.exists():
            raise forms.ValidationError('this phone number does not exists')
        return self.cleaned_data['phone']  

class VerfiyCodeForm(forms.Form):
    code=forms.IntegerField()