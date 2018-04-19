from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)

def travel(request):
	return render(request, 'travel.html')

def travel_post(request):
	ctx = {}
	if request.POST:
		ctx['name'] = request.POST['name']
		ctx['email'] = request.POST['email']
		ctx['phone'] = request.POST['phone']
		ctx['message'] = request.POST['message']
	return render(request, 'travel_post.html', ctx)
