from django.shortcuts import render,redirect
from .models import DummyDetail
from django.views.generic import (ListView,
								  DetailView,
								  CreateView,
								  UpdateView,
								  DeleteView)
#from django.contrib.auth.decorators import login_required

# Create your views here.
posts=[
 
	{
		"userId":1,
		"id":1,
		"title":"Django",
		"body":"Django Content"
	},

	{
		"userId":2,
		"id":2,
		"title":"Angular",
		"body":"Angular Content"
	},

	{
		"userId":1,
		"id":3,
		"title":"ReactJs",
		"body":"ReactJs Content"
	}
]


users=[
	{
		"id":1,
		"name":"sana"
	},
	{
		"id":2,
		"name":"sudha"
	}
]

def home(request):
	context = {
		'posts' : posts,
		'users':  users

	}
	return render(request,"courses/home.html",context)
#@login_required
class DummyListView(ListView):
	model = DummyDetail
	template_name = 'courses/dummyDetails.html'
	context_object_name = 'details'

class DummyDetailView(DetailView):
	model = DummyDetail
class DummyCreateView(CreateView):
	model = DummyDetail
	fields='__all__'

class DummyUpdateView(UpdateView):
	model = DummyDetail
	fields = '__all__'

class DummyDeleteView(DeleteView):
	model = DummyDetail
	template_name = "courses/dummydetail_delete.html"
	success_url = '/mycourses'

def form_valid(self,form):
	return super().form_valid(form)

def dummies(request):
	details=DummyDetail.objects.all()
	context={
		'details':details
	}
	
	return render(request,"courses/dummyDetails_1.html",context)

def addDummies(request):
	if request.method == "POST":
		details = DummyDetail(name=request.POST['name'],
							  gender=request.POST['gender'],
							  mobile=request.POST['mobile'],
							  email=request.POST['email'])
		details.save()
		
		return redirect('/courses/details')
		
	else:
		return render(request,"courses/addDetails.html")

def editDummies(request,dummy_id):
	if request.method == "POST":
		getDummy = DummyDetail.objects.get(id=dummy_id)
		getDummy.name=request.POST['name']
		getDummy.gender=request.POST['gender']
		getDummy.mobile=request.POST['mobile']
		getDummy.email=request.POST['email']
		getDummy.save()





		return redirect('/courses/details')
	else:
		getDummy = DummyDetail.objects.get(id=dummy_id)
		context = {"details":getDummy}
		return render(request,'courses/editDetails.html',context)

def deleteDummies(request,dummy_id):
	getDummy = DummyDetail.objects.get(id=dummy_id)
	getDummy.delete()
	return redirect('/courses/details')