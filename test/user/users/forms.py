from django import forms
from .models import User , Group
from django.forms import ModelForm , TextInput , Textarea


class UserForm(forms.Form):
	nickname = forms.CharField()
	groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

class GroupForm(forms.Form):

	name = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)

