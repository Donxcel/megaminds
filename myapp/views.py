from django.shortcuts import render,redirect
from .forms import Service
from .models import Addservice
# Create your views here.
''' WE will use the function to display the home page and the service page'''
project_list = Addservice.objects.all()


# creating the home page

def home(request):
    content = Addservice.objects.all()
    return render(request,'myapp/about.html',{'content':content})
# creating a an add service functionality

def add_service(request):
    # checking for valid post requests
    service_create = None
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        service_create = Addservice.objects.create(service_name=name,
                                                   service_description=description
                                                   ,service_image=image)
        service_create.save()
        return redirect('home')
    return render(request,'myapp/test.html',{'form':service_create})


def ViewService(request):
    service_list = Addservice.objects.all()
    return render(request,'myapp/service.html',{'service_list':service_list})

""" VIewing the project page and it's content  """

def ViewProject(request):
    return render(request,'myapp/project.html',{'project_list':project_list})


''' pricing page'''
def pricing(request):
    return render(request,'myapp/pricing.html')

def contact(request):
    return render(request,'myapp/contact.html')

def about(request):
    return render(request,'myapp/about.html')

def index(request):
    return render(request,'myapp/index.html')

def index_2(request):
    return render(request,'myapp/index-2.html')

def index_3(request):
    return render(request,'myapp/index-3.html')

def index_4(request):
    return render(request,'myapp/index-4.html')