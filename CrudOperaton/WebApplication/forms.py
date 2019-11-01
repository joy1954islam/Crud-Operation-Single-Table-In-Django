from django import forms

from WebApplication.models import GovernmentEmployee


class GovernmentEmployeeForm(forms.ModelForm):
    class Meta:
        model = GovernmentEmployee
        fields = "__all__"