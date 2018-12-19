from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"your full name"
        }))
    email    = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"your email"
        }))
    content  = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder":"your message"
        }))
    def clean_email(self):
        email= self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gmail")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    PINCODE_CHOICES= [
    ('orange', '421 503'),
    ('cantaloupe', '421 501'),
    ('mango', '421 502'),
    ('honeydew', '421 504'),
    ]
    businessName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"your Business Name",
        "id":"businessName"
        
        }))
    Building = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"Building",
        "id":"Building"
        
        }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"street",
        "id":"street"
        
        }))
    landmark = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"landmark",
        "id":"landmark"
        
        
        }))
    area = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"area",
        "id":"area"
        
        
        }))

    city = forms.CharField(label='City ',widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"city",
        "id":"city"
        
        }))
    pincode = forms.CharField(label='PIN Code ',widget=forms.Select(choices=PINCODE_CHOICES, attrs={
        "class": "form-control col-md-3",
        "value":"default",
        "id":"pincode"
        
        }))
    
    state = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"state",
        "id":"state"
        
        
        }))
    country = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"country",
        "id":"country"
        
        
        }))
    #email    = forms.EmailField(widget=forms.EmailInput(attrs={
     #   "class": "form-control",
      #  "placeholder":"your email"
       # }))
    
    #password = forms.CharField(widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    def clean_username(self):
        username= self.cleaned_data.get('username')
        qs= User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email= self.cleaned_data.get('email')
        qs= User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("email is already taken")
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password Must Match!!")
        return data
        
class RegisterForm2(forms.Form):
    businessName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"your Business Name",
        "id":"businessName"
        
        }))
    Building = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"Building",
        "id":"Building"
        
        }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"street",
        "id":"street"
        
        }))
    landmark = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"landmark",
        "id":"landmark"
        
        
        }))
    
class RegisterForm3(forms.Form):
    PINCODE_CHOICES= [
    ('orange', '421 503'),
    ('cantaloupe', '421 501'),
    ('mango', '421 502'),
    ('honeydew', '421 504'),
    ]
    businessName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"your Business Name",
        "id":"businessName"
        
        }))
    Building = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"Building",
        "id":"Building"
        
        }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"street",
        "id":"street"
        
        }))
    landmark = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"landmark",
        "id":"landmark"
        
        
        }))
    
class RegisterForm4(forms.Form):
    businessName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"your Business Name",
        "id":"businessName"
        
        }))
    Building = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"Building",
        "id":"Building"
        
        }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"street",
        "id":"street"
        
        }))
    landmark = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control col-md-3",
        "placeholder":"landmark",
        "id":"landmark"
        
        
        }))    
