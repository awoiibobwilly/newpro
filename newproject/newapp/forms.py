from django import forms #importing form from django

class TaskForm(forms.Form): #inheriting the class to extend functionality
    name = forms.CharField(max_length=200, widget = forms.TextInput(attrs={'class': 'form-control'}), required=False)
    details = forms.CharField(max_length=1000, widget = forms.TextInput(attrs={'class': 'form-control'}), required=False)
    number_of_people = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    date = forms.DateField(widget = forms.DateInput(attrs={'class': 'form-control'}), required=False)
    day_of_week = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        details = cleaned_data.get('details')
        number_of_people = cleaned_data.get('number_of_people')
        date = cleaned_data.get('date')
        day_of_week = cleaned_data.get('day_of_week')

        if not name:
            self.add_error('name', 'Please provide a name')
        elif len(name) < 3:
            self.add_error('name', 'Name must be at least 3 characters')

        return cleaned_data



    
    
