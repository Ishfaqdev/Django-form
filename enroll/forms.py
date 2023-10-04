from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=20, error_messages={
        "required": "Your name must not be empty!",
        "max_length": "Please enter a shorter name",
    })
    department = forms.CharField(label="Department")
    semester = forms.IntegerField(label="Semester", min_value=1, max_value=8, error_messages={
        "required": "Please enter your semester!",
        "max_length": "Should be between 1-8", })
