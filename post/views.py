from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


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
