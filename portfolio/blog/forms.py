from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class Subscribe(forms.Form):
    contact_name=forms.CharField(label='',required=True)
    contact_email=forms.CharField(label='',required=True)
    content=forms.CharField(label='Your message:',required=True,widget=forms.Textarea)
