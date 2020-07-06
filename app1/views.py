from .models import Subscribe,myblog,Contact,Gallery
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_GET


# Create your views here.
def index(request):
    blogData = myblog.objects.all().filter(featured=True).order_by('-blog_id')
    if request.method == "POST":
        Email = request.POST.get('email')
        if(Email !=""):
            sub = Subscribe(email = Email)
            sub.save()
            messages.add_message(request, messages.SUCCESS, 'Thankyou for Subscription')
        else:
            messages.add_message(request, messages.WARNING, 'Kindly Enter Your Email')
    gallery = Gallery.objects.all().filter(featured=True).order_by('-image_id')
    return render(request, 'index.html', {
    "blog" : blogData,
    "gallery":gallery
    })

def projects(request):
    return render(request, 'projects.html', {

    })

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name !="" and email != "" and subject !="" and message !="":
            sendmessage = Contact(personname = name, email = email, subject =subject, message = message)
            sent = sendmessage.save()
            messages.add_message(request, messages.SUCCESS, 'ThankYou Form Contacting Us, We will get you soon!')
        else:
            messages.add_message(request, messages.WARNING, 'Please Fill the Form Correctly!')
    return render(request, 'contact.html', {

    })

def about(request):
    return render(request, 'about.html', {

    })

def gallery(request):
    gallery = Gallery.objects.all().order_by('-image_id')
    return render(request, 'gallery.html', {
        "gallery":gallery
    })


def blog(request,id):
    blog = myblog.objects.get(blog_id=id)
    nextpost = myblog.objects.filter(blog_id__gt=blog.blog_id).order_by('blog_id').first()
    prevpost = myblog.objects.filter(blog_id__lt=blog.blog_id).order_by('blog_id').last()
    print('hello')
    return render(request, 'blog-post.html', {
        "blog":blog,
        "nextpost":nextpost,
        "prevpost":prevpost
    })

def bloglist(request):
    blogData = myblog.objects.all().order_by('-blog_id')
    paginator = Paginator(blogData, 3)
    page = request.GET.get('page')
    blogData = paginator.get_page(page)
    return render(request, 'blog-list.html', {
    "blog" : blogData,
    'post': blogData
    })

def search(request):
    query= request.GET['query']
    if len(query)>32:
        blog = ""
    elif len(query)<3:
        blog = ""
    else:
        blog = myblog.objects.filter(blog_title__icontains = query)
    return render(request,'search.html',{
        "blog":blog,
        "query":query
        })

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: admin",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
# def user(request):
#     if request.method=="POST":
#         form = AuthenticationForm(request = request, data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username = username, password =password)
#             if user is not None:
#                 messages.success(request, f"You are now logged in as {username}")
#                 return redirect('home')


#     return render(request, 'login.html')


# def register(request):
#     # FormData = userForm
#     # if request.method == "POST":
#     #     form = userForm(request.POST)
#     #     data = form.save()
#     #     if (data):
#     #         messages.success(request, 'Successfully Register')
#     #     else:
#     #         messages.error(request, 'Kindly Fill the Form Correctly')

#     return render(request, 'register.html',{
#         # "form": userForm
#     })