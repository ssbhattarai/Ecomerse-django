from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Email"}))
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Your contents"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm_pass = forms.CharField(
        label="Confirmed Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(
                "username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        confirm_pass = self.cleaned_data.get("confirm_pass")
        if confirm_pass != password:
            raise forms.ValidationError("password must match.")
        else:
            return data
