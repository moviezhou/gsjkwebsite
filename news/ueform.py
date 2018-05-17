from django import forms
from ueditor.ueditor_widget import UEditorWidget

class UEditorForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=UEditorWidget)