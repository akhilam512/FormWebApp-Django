from django import forms

from .models import User


class UserForm(forms.ModelForm):
	class Meta:
		model 	= User
		fields 	=	[
			'name',
			'age',
			'email',
			'password',
			'gender',
		] 

	def clean_name(self):  # validation
		name = self.cleaned_data.get("name")

		if name == "hello":
			raise forms.ValidationError("Not a valid name")

		return name

