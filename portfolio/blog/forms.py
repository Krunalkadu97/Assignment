from django import forms

class Subscribe(forms.Form):
    contact_name=forms.CharField(label='Enter your company/your name:',required=True)
    contact_email=forms.CharField(label='Enter your company/your Email:',required=True)
    content=forms.CharField(label='Your message:',required=True,widget=forms.Textarea)
