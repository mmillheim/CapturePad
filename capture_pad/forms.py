from django import forms
from .models import Notebook, Year, Month, Day, Note

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ('title', 'active')

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ('name', 'notebook')

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ('name', 'year')

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('name', 'date', 'month')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('textContent', 'complete', 'date', 'dueDate', 'day')