from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from doctorblogapp.models import Blog, User, Categories
from django.contrib import messages
from .form import FileUploadForm
import hashlib
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import redirect
from datetime import datetime
import os

# Create your views here.

def index(request):
    blogData = Blog.objects.filter(status = 1).values()
    context = {

        'data' : blogData
    }
    
    return render(request, 'index.html', context)

def login(request):
    if not 'id' in request.session or not request.session['id']:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            password = hashlib.md5(password.encode()).hexdigest()

            blogData = User.objects.filter(email= email, password= password).values()
            context = {
                'data' : blogData
            }
            if blogData:
                userData = User.objects.get(email= email, password= password)
                request.session['id'] = userData.id
                return redirect('doctorBlog')
            return render(request, 'login.html', context)
        return render(request, 'login.html')
    return redirect('doctorBlog')
    

def doctorBlog(request):
    if not 'id' in request.session or not request.session['id']:
        return redirect('login')
    
    blogData = Blog.objects.filter(userId = request.session['id'], status = 1).values()
    context = {
        'data' : blogData
    }
    return render(request, 'doctorBlog.html', context)


def add(request):
    if not 'id' in request.session or not request.session['id']:
        return redirect('login')
    
    if request.method == "POST":
        data = {}
        if request.POST.get('id'):
            id = request.POST.get('id')
            data['id'] = int(id)
            existing_record = get_object_or_404(Blog, id=data['id'])
        else:
            existing_record = None

        data['userId'] = request.session['id']
        if request.POST.get('title'):
            data['title'] = request.POST.get('title')
        if request.POST.get('summary'):
            data['summary'] = request.POST.get('summary')
        if request.POST.get('content'):
            data['content'] = request.POST.get('content')
        if request.POST.get('categoryId'):
            data['categoryId'] = int(request.POST.get('categoryId'))

        if len(request.FILES) != 0:
            uploaded_image = request.FILES.get('blog_image')
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            # Extract file extension from the original file name
            _, file_extension = os.path.splitext(uploaded_image.name)

            # Construct the new file name with the timestamp
            new_file_name = f"{timestamp}{file_extension}"
            
            new_file_path = os.path.join(f"{settings.MEDIA_ROOT}/upload", new_file_name)

            default_storage.save(new_file_path, uploaded_image)
            data['blog_image'] = new_file_name
            request.FILES['blog_image'] = new_file_name
            form = FileUploadForm(data, request.FILES , instance=existing_record)
            if form.is_valid():
                form.save()
        if request.POST.get('id'):
            id = int(request.POST.get('id'))
            Blog.objects.filter(id = id).update(**data)
        else:
            blog = Blog(userId_id = data['userId'],  categoryId_id = data['categoryId'], title = data['title'], summary = data['summary'], content = data['content'], blog_image = data['blog_image'])

            blog.save()
            messages.success(request, "You Message has been sent!")
        return redirect('doctorBlog')
    


    categories = Categories.objects.filter(status= 1).values()
    context = {
        "categories" : categories
    }
    return render(request, 'add.html', context)

def edit(request, id):
    edit = Blog.objects.get(id = id, userId = request.session['id'])
    categories = Categories.objects.filter(status= 1).values()
    
    context = {
        "edit" : edit,
        "id" : id,
        "categories" : categories
    }
    return render(request, 'add.html', context)

def delete(request, id):
    if id:
        deleted = Blog.objects.filter(id = id, userId = request.session['id']).count()

        if deleted:
            data = {
                "status" : 2
            }
            Blog.objects.filter(id = id).update(**data)
            messages.success(request, "You Message has been deleted")
            return redirect('doctorBlog')
        messages.warning(request, "You Message has been deleted")
        return redirect('doctorBlog')
    return redirect('doctorBlog')
def logout(request):
    del request.session['id']

    context = {
        
    }

    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(hashlib.md5(password.encode()))
        print(hashlib.md5(password.encode()).hexdigest())
        print(type(hashlib.md5(password.encode()).hexdigest()))
        userData = User(name = name, email= email, password = hashlib.md5(password.encode()).hexdigest())
        userData.save()
        request.session['id'] = userData.id

        return redirect('doctorBlog')
    
    context = {

    }
    return render(request, 'signup.html', context)
    