from wagtail.core.blocks.field_block import FieldBlock
from django import forms
from ueditor.ueditor_widget import UEditorWidget
from django.utils.safestring import mark_safe

class UEditorBlock(FieldBlock):

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, **kwargs):
        self.field = forms.CharField(
            required=required, help_text=help_text, max_length=max_length, min_length=min_length,
            widget=UEditorWidget)
        super().__init__(**kwargs)

    def get_default(self):
        return mark_safe(self.meta.default or '')

    def to_python(self, value):
        return mark_safe(value)

    def get_prep_value(self, value):
        # explicitly convert to a plain string, just in case we're using some serialisation method
        # that doesn't cope with SafeText values correctly
        return str(value) + ''

    def value_for_form(self, value):
        # need to explicitly mark as unsafe, or it'll output unescaped HTML in the textarea
        return str(value) + ''

    def value_from_form(self, value):
        return mark_safe(value)

    class Meta:
        icon = 'code'