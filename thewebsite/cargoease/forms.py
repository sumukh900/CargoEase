from django import forms
from .models import User
from .models import Carrier
from .models import Route



class ConsigneeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password', 'email', 'contact_number', 'address']
        widgets = {
            'password': forms.PasswordInput,
            'confirm_password': forms.PasswordInput,
        }
class CarrierSignUpForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = ['carrier_id','company_name', 'contact_number', 'email_address', 'address', 'first_name', 'last_name', 'password','price']
        widgets = {'password': forms.PasswordInput,
	}

class NewRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_id','source', 'destination', 'distance','carrier_id']