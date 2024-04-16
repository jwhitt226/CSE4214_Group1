from store.models import User, Customer, Seller
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomerSignUpForm(forms.ModelForm):
    fname = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control ', 'placeholder': 'First Name'}))
    lname = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Last Name'}))
    address = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Address'}))
	
    class Meta:
        model = Customer
        fields = ('fname', 'lname', 'address', )
		
class SellerSignUpForm(forms.ModelForm):
    name = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Name'}))
    address = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Address'}))
	
    class Meta:
        model = Seller
        fields = ('name', 'address', )
		

# class SignUpForm(UserCreationForm):
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    type = forms.ChoiceField(label="", choices=User.Types.choices, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('userID', 'email', 'password1', 'password2', 'type')

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['userID'].widget.attrs['class'] = 'form-control form-floating my-3'
            self.fields['userID'].widget.attrs['placeholder'] = 'User Name'
            self.fields['userID'].label = ''
            self.fields['userID'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'