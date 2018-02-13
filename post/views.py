from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Post
from .forms import UserForm


def index(request):
	post = Post.objects.all()[:10]

	context ={
		'title': 'Latest Announcements',
		'post': post
	}
	return render(request,'post/index.html',context)


def details(request, id):

	post = Post.objects.get(id=id)

	context ={

		'post' : post
	}

	return render(request,'post/details.html', context)	

class UserFormView(View):
	form_class = UserForm
	template_name = 'post/registration_form.html'

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
					return redirect('post:index')


		return render(request, self.template_name, {'form': form})




















