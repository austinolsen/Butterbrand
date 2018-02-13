# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

class UserFormView(View):
	form_class = UserForm
	template_name = 'main_app/registration_form.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#Process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			#Creates object from form, but doesn't save to database
			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('main_app:index')


		return render(request, self.template_name, {'form': form})