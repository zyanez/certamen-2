from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ["content", "important"]
        
    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Contenido vacio")
        if len(content) > 120:
            raise forms.ValidationError("El maximo de caracteres es de 120")
        return content