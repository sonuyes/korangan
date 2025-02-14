from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .forms import regform
from .models import reg
# Create your views here.
l=0
def index(request):
    if request.method=="POST":
        form=regform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            last_object = reg.objects.latest('id') 
            reg_object = reg.objects.get(id=last_object.id)
    
            lk=str(reg_object.email)
            lkim=str(reg_object.image)
            ko=open("C:/Users/SONU PHILIP/Documents/fish/fish/templates/kk.html","a")
            po=open("C:/Users/SONU PHILIP/Documents/fish/fish/templates/kk.html","r")
            if lkim=="":
                print(lkim)
                ko.write("<div class="+"chat-bubble"+">"+lk+"</div><!--h-->")
            else:
                ko.write("<div class="+"chat-bubble"+">"+lk+"<img class="+"'chat-bubble img'"+" src="+"'media/"+lkim+"'"+"></div><!--h-->")
                print(lkim)
            ko.close()
            po.close()


            
            checkf=open("C:/Users/SONU PHILIP/Documents/fish/fish/templates/index.html","r")
            kp=str(int(checkf.read())+1)
            checkf.close()
            check=open("C:/Users/SONU PHILIP/Documents/fish/fish/templates/index.html","w")
            check.write(kp)
            check.close()

            

            return JsonResponse({
                'message': "success"
              })
        else:
            print(form.errors)
    form=regform()
    dict_form={
        'form':form,
        'regh':reg.objects.all()
    }
    
    return render(request,'indexx.html',dict_form)


def inp(request):
    return render(request,'kk.html')


def check(request):
    return render(request,'index.html')


