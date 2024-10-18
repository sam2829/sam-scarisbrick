from django import forms


class ContactForm(forms.Form):
    """
    class for the email form
    """
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea, max_length=500,)
