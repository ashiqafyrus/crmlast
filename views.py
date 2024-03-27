from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from .models import ImageApp,Archive
from django.contrib.auth import logout
# Create your views here.
def home(request):
     return render(request,'home.html')
def about(request):
     return render(request,'about.html')
def services(request):
     return render(request,'services.html')
def login(request):
     return render(request,'login.html')
def crmpage(request):
     return render(request,'crm.html')
def crmcontent(request):
     return render(request,'crmcontent.html')
def drag(request):
     return render(request,'drag.html')
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
   
    return redirect('crmloginpage')
def demo(request):
    return render(request,'demo.html')
def save_image(request):
    if request.method == 'POST':
        image_data = request.FILES.get('image')  # Assuming the image data is sent as a file
        if image_data:
            # Save the image data to the database
            image = ImageApp(image_data=image_data)
            image.save()
            return JsonResponse({'message': 'Image saved successfully'}, status=200)
    return JsonResponse({'message': 'Invalid request'}, status=400)
def appdetails(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        
        data=ImageApp(name=name,price=price)
        data.save()
        
        return redirect('drag')
def crmloginpage(request):
     product=ImageApp.objects.all()
     archived_app_ids = Archive.objects.values_list('app_id', flat=True)
     return render(request,'crmnavbar.html',{'product':product,'archived_app_ids': archived_app_ids})

def archive_app(request, id):
    product = ImageApp.objects.get(id=id)
    data, created = Archive.objects.get_or_create(app=product)
    if created:
        # Optionally, do something if the object was newly created
        pass
    else:
        # Optionally, do something if the object already existed
        pass
    data.save()
    return redirect('crmloginpage')
def crmarchive(request):
    
    arch=Archive.objects.all()
    return render(request,'archeive.html',{'arch':arch})
def archiveremove(request, id):
    product = Archive.objects.get(id=id)
    product.delete()
    return redirect('crmarchive')
def log_out(request):
    # Your logout logic here
    # For example, if you are using Django's built-in logout function:
    from django.contrib.auth import logout
    logout(request)
    
    # Redirect to the home page
    return redirect('crmcontent')  