from django.shortcuts import render
from.models import Objective

# Create your views here.

def home(request):
	return render(request,'portal/base.html')


def index(request):
	datas=Objective.objects.all()
	context={'datas':datas}
	return render(request,'portal/home.html',context)



def object(request):
	if request.method=="POST":
		obj=Objective(Objective=request.POST['objective'],
						mission=request.POST['mission'],
						vision=request.POST['vision'])
		details.save()
		return redirect("/portal/base")
	else:
		return render(request,'portal/object.html')
