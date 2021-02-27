from django.shortcuts import render
from .form import ImageForm
from .models import ImageEncrytion
from .image_encryption_logic import encode as e

# Create your views here.
def encryption(request):
    if request.method == "POST":
        if(ImageEncrytion.objects.all().count() >=2):
                img_records = ImageEncrytion.objects.all()
                for i in img_records:
                    i.delete()
                    break
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            img=ImageEncrytion.objects.all()
            form=ImageForm()   
            if img.count() == 2: 
                count = True 
            else:
                count = False
            return render(request,"encryption.html", {"obj":obj, "img":img , "form": form, "countIs2": count})  
    else:
        form=ImageForm()    
        img=ImageEncrytion.objects.all()
    return render(request,"encryption.html",{"img":img,"form":form})


def get_encrypted_image(request):
    image_list = ImageEncrytion.objects.all()
    parameter_list = []
    for entry in image_list:
        parameter_list.append("media/"+str(entry.image))
    for entry in image_list:
        parameter_list.append(entry.text)
        break
    op_path = e.encryptImage(parameter_list)
    return render(request,"encryptionresult.html", {'img_path': op_path})