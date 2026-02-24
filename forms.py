from django import forms
from django.utils.translation import gettext_lazy as _

from .models import StoreSettings, OnlineOrder

class StoreSettingsForm(forms.ModelForm):
    class Meta:
        model = StoreSettings
        fields = ['store_name', 'is_active', 'currency', 'allow_guest_checkout']
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle'}),
            'currency': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'allow_guest_checkout': forms.CheckboxInput(attrs={'class': 'toggle'}),
        }

class OnlineOrderForm(forms.ModelForm):
    class Meta:
        model = OnlineOrder
        fields = ['order_number', 'customer_email', 'customer_name', 'status', 'subtotal', 'tax_amount', 'total', 'shipping_address', 'notes']
        widgets = {
            'order_number': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'customer_email': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'email'}),
            'customer_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'subtotal': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'tax_amount': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'total': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'shipping_address': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

