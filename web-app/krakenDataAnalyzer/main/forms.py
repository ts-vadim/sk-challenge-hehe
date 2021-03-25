from django import forms

class RecordForm(forms.Form):
    record_file = forms.FileField()