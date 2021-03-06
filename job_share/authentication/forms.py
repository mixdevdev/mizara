from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2","is_employer",
                "is_trainer",
                "is_user")

    def save(self,commit=True):
        user=super(NewUserForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class Login_user(forms.Form):
#     username=forms.CharField(max_length=200,label="Username")
#     password=forms.CharField(max_length=200,label="Password",widget=forms.PasswordInput)
