from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import Image
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def notesPage(request):
    context = {}
    return render(request, 'home/notes.html', context)