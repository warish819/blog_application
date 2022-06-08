# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login


# from user.forms import UserForm

# # Create your views here.
# def registration(request):
#     if request.method == 'POST':
#         user = UserForm(request.POST)
#         if user.is_valid():
#             user.save()
#             return redirect("/")
#     else:
#         user = UserForm()
#         return render(request,'registration.html',{'user':user})        

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/")
#     else:
#         # return HttpResponse("Invalid credentials")
#         return render(request,'login.html')
  


from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from user.forms import  SignUpForm
from django.contrib import messages
from blog_app.models import Blog


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
                messages.info(request, f"You are now logged in as {username}.")
            else:
                
                messages.error(request,"Invalid username or password.")
        else:
            return HttpResponse("Invalid username or password")

            
    form = AuthenticationForm()
    return render(request,"login.html",{'login_form':form})

def logout(request):
    auth.logout(request)
    return render(request,'login.html')  

def confirmation(request):
    return render(request,'confirmation.html')      

     




               
     
    

    
        
              
   

        
    
