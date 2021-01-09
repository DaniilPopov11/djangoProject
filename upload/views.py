from django.shortcuts import render
from django.http import HttpResponse
from upload.functional import handle_upload_file
from upload.forms import Clients



def upload(request):
    if request.method == 'POST':
        customer = Clients(request.POST, request.FILES)
        if customer.is_valid():
            handle_upload_file(request.FILES['deals'])
            model_instance = student.save(comit=False)
            model_instance.save()
            return HttpResponse("File upload successfully")
    else:
        customer = Clients()
        return render(request, "upload.html", {'form': customer})
