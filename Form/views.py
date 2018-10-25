from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.views import View
# Create your views here.
#from .models import User
#from .form import UserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect 

class AboutView(TemplateView):
	template_name = "about.html"

class HomeView(TemplateView):
	template_name = "home.html"

# def signup(request):
# 	form = UserForm(request.POST or None)
	

# 	errors = None

# 	if form.is_valid():
# 		form.save()
# 		form = UserForm()
# 		#print("DONEEEEE-----!!!!!!!!!!!!!!!!!!!!!!!!!")

# 	if form.errors:
# 		errors = form.errors

# 	template_name = "signup.html"
# 	context = {"form":form, "error":errors}

# 	return render(request, template_name, context)



class SignUpView(TemplateView):
	template_name = "signup.html"
	form_class = UserCreationForm
	initial = {'key' : 'value'}


	def get(self, request, *args, **kwargs):
		form = self.form_class(initial = self.initial)
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')

			user = authenticate(username=username, password=raw_password)
			login(request, user)		

			print("\n\n-------------------logged in-----------!!!!!!!!!!!!! " + username)
			return redirect('/success/')

		return render(request, self.template_name, {'form' : form})

class LogInView(TemplateView):
	template_name = "login.html"
	form_class = UserCreationForm
	initial = {'key' : 'value'}


	def get(self, request, *args, **kwargs):
		form = self.form_class(initial = self.initial)
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()


class SuccessView(TemplateView):
	template_name = "success.html"

	