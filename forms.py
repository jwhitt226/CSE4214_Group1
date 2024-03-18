from django import forms
import uuid

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller'), ('admin', 'Admin')])

    def generate_userid(self):
        # Generate a unique user ID using uuid.uuid4()
        return str(uuid.uuid4())[:5]

    def create_user(self):
        userid = self.generate_userid()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        state = self.cle
