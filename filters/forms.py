from django import forms
from filters.models import UserFilter


class NewFilterForm(forms.Form):
    system_name = forms.SlugField(max_length=50)


class FilterTestForm(forms.Form):
    test_obj = forms.CharField()


class FilterTestUserForm(forms.Form):
    user = forms.CharField()


class UserFilterForm(forms.ModelForm):
    class Meta:
        model = UserFilter
        fields = ('name', 'value',)
