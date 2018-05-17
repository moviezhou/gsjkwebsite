from django.forms import widgets

class UEditorWidget(widgets.Input):
    template_name = 'placeholder.html'
    input_type = 'text'
    def get_context(self, name, value, attrs):
        context = super(UEditorWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['placeholder'] = name.title()
        return context
