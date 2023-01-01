from django import forms 

from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget= forms.PasswordInput())
    password2 = forms.CharField(label='Re-enter password', widget= forms.PasswordInput()) 
    date_of_birth = forms.CharField(label='Date of Birth', widget =  forms.TextInput(attrs={
        'type':'date'
    }))


    class Meta:
        model = CustomUser
        fields =  ('firstname','lastname', 'email')
    
    def clean_password2(self) -> str:
        cd =self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError('Error, passwords didn\'t match')
        return cd['password2']

class CustomUserChangeForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('firstname','lastname', )
