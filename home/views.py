from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image, Notes
from .forms import NotesForm
from django.http import HttpResponseRedirect

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form':form}
    return render(request, 'home/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'home/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    obj=Image.objects.all()
    return render(request, 'home/index.html',{'image':obj})

@login_required(login_url='login')
def detail_view(request, id, slug):
    obj=get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'home/detail.html',{'image':obj})

@login_required(login_url='login')
def search(request):
    query=None
    result=[]
    if request.method == 'GET' :
        query=request.GET.get('search')
        result=Image.objects.filter(Q(title__icontains=query) | Q(sname__icontains=query) | Q(tags__icontains=query)
                                    | Q(sdesc__icontains=query) | Q(ldesc__icontains=query))
    return render(request, 'home/search.html',{'query':query, 'result':result})

def notes_view(request):
    notes = Notes.objects.all()
    context = {'notes': notes }
    return render(request, 'home/notes.html', context)

def add_notes(request):
    if request.method == 'POST':
        plantname = request.POST.get('plantname')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if Notes:  # Check if the image was uploaded
            new_image = Notes(plantname=plantname, description=description, image=image)
            new_image.save()
            valid_message = "New post plant added!"
            return render(request, 'home/add_notes.html', {'valid': valid_message})  # Redirect after successful upload
        else:
            # You can add an error message here to inform the user
            error_message = "Please upload a valid image."
            return render(request, 'home/add_notes.html', {'error': error_message})

    return render(request, 'home/add_notes.html')
