from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import ResgiterFrom
# Create your views here.
def index(request):
    return render(request,"home.html")
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        print(username)
        if User.objects.filter(username=username):
            messages.warning(request, 'Username is already exist')
            return redirect('signup')
        else:
            password=request.POST['password']
            corfirm_password=request.POST['repass']
            if password==corfirm_password:
                              user=User.objects.create(                               
                                username=username,
                                password=password
                                    
                              )
                              user.save()
                              return redirect('userlogin')
    return render(request,'resgister.html')


def userlogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
                messages.warning(request, 'User is Not Exist')
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('newpage')
    

        # if user is not None:
        #     login(request,user)
        #     messages.success(request, f'Hi {user.username}, Welcome To GETLAPS')
        #     return redirect('home')
        # else:
        #     messages.warning(request, 'invalid Credential')
    
    return render(request,'login.html')

# def userlogout(request):
#     logout(request)
#     return redirect('home')
def resgiter(request):
    if request.method=='POST':
        form=ResgiterFrom(request.POST)
        if form.is_valid():   
            form.save()
            return render(request,'confimations.html')
    form=ResgiterFrom()
    dict_form={
         'form':form
    }
    return render(request,'newpage.html',dict_form)
    