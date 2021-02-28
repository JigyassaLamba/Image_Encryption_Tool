from django.shortcuts import render
from .form import ImageForm
from .models import ImageDecryption
from .image_decryption_logic import decode as d
# Create your views here.
def decryption(request):
    if request.method == "POST":
        if(ImageDecryption.objects.all().count() >=1):
                img_records = ImageDecryption.objects.all()
                for i in img_records:
                    i.delete()
                    break
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            img=ImageDecryption.objects.all()
            form=ImageForm()   
            if img.count() == 1: 
                count = True 
            else:
                count = False
            return render(request,"decryption.html", {"obj":obj, "img":img , "form": form, "countIs1": count})  
    else:
        form=ImageForm()    
        img=ImageDecryption.objects.all()
    return render(request,"decryption.html",{"img":img,"form":form})


def get_decrypted_image(request):
    image_list = ImageDecryption.objects.all()
    parameter_list = []
    for entry in image_list:
        parameter_list.append("media/"+str(entry.image))
    for entry in image_list:
        parameter_list.append(entry.text)
        break
    op_path = d.decryptImage(parameter_list)
    return render(request,"decryptionresult.html", {'img_path': op_path})