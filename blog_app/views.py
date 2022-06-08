
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from blog_app.models import Blog

from user.forms import BlogsForm, ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":        
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid information")    
    else:
        form = ContactForm()
        return render(request,'contact.html',{'form':form})   

def blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.filter(status='published').order_by('-published_at')
        return render(request,'blog.html',{'blogs':blogs}) 
    return render (request,'blog.html')
    

def create_blog(request):
    if request.method == 'POST':
        blog = BlogsForm(request.POST)
        if blog.is_valid():
            blog.save()
            return redirect('/dashboard')
        else:
            return HttpResponse("Invalid input")    
    else:
        blog = BlogsForm() 
    return render(request,'create_blog.html',{'blog':blog})   

def about(request):
    return render(request,'about.html')  

def dashboard(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/')
        else:
            return HttpResponse("Invalid information! Try again...")  
    else:
        form = ContactForm()       
    return render(request,'index.html',{'form':form})
    
         
def blog_dashboard(request):
    if request.method == 'GET':
        blogs = Blog.objects.filter(status='published').order_by('-published_at')
        return render(request,'index.html',{'blogs':blogs}) 
    return render (request,'index.html')

# def search_posts(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')

#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(title__icontains=query) | Q(content__icontains=query)

#             results= Blog.objects.filter(lookups).distinct()

#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'index.html', context)

#         else:
#             return render(request, 'index.html')

#     else:
#         return render(request, 'index.html')

        
    
    

                       
            

    
        
   
 
    