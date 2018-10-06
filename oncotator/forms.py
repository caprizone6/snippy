from django import forms
from models import CSVFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class FileForm(forms.ModelForm):

    class Meta:
        model = CSVFile
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', label=' ',),
            Field('file', required=False)
        )



