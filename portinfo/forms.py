from django import forms



class Contact_Me_Form(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
            'class':"form-control",
            "name":"name",
            "id":"name",
            "type":"text",
            "data-sb-validations":"required",
            "placeholder":"Enter your name..."
        }))
    email = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
            'class':"form-control",
            "name":"email",
            "id":"email",
            "type":"email",
            "data-sb-validations":"required",
            "placeholder":"Enter your email..."
        }))
    phone = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
            'class':"form-control",
            "name":"phone",
            "id":"phone",
            "type":"tel",
            "data-sb-validations":"required",
            "placeholder":"Enter your phone number"
        }))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
            'class':"form-control",
            "name":"message",
            "id":"message",
            "type":"text",
            "data-sb-validations":"required",
            "placeholder":"Enter your message..."
        }))
    