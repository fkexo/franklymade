from django import forms
from django.db.models import fields
from django.forms import TextInput
from crispy_forms.helper import FormHelper


from .models import PythonCourse

from tinymce.widgets import TinyMCE




class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostCourseForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols':30, 'rows':10}
        )
    )

    def __init__(self, *args, **kwargs):
        super(PostCourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    class Meta:
        model = PythonCourse
        # select the field we need in the create form

        fields = ('title', 'description', 'content')


       
