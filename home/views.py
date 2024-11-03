from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.db.models import Q
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image, Notes
from .forms import NotesForm
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash #edit profile
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
import logging
import os
from .models import Notes


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
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Plant Notes Added Successfully")
            return redirect('notes')
    else:
        form = NotesForm()
    
    return render(request, 'home/add_notes.html', {'form': form})

def user_list(request):
    users = User.objects.all()  # Get all users
    return render(request, 'home/user_list.html', {'users': users})

def add_user(request):
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

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password:
            if password == confirm_password:
                user.password = make_password(password)
            else:
                messages.error(request, "Passwords do not match.")
                # Return the same template with the error message
                return redirect('index') #render(request, 'home/index.html', {'user': user}) # Replace with the actual URL name for this view

        user.save()
        messages.success(request, 'User details updated successfully!')
        return redirect('login')

    return render(request, 'home/index.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User account deleted successfully!')
    return redirect('user_list')

#edit profile

def profile(request):
    return render(request, 'home/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Update name and username
        
        user.username = username

        # Check and update password
        if password:
            if password == confirm_password:
                user.password = make_password(password)
            else:
                messages.error(request, "Passwords do not match.")
                return redirect('profile_update')  # Replace with the actual URL name for this view

        # Save the user profile
        user.save()
        messages.success(request, 'Profile Updated Successfully.')
        return redirect('login')

    return redirect('login')


def edit_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = get_object_or_404(Notes, id=note_id)
        form = NotesForm(request.POST, request.FILES, instance=note)
        
        if form.is_valid():
            form.save()
            return redirect('notes')  # redirect to the notes page after saving changes
    return redirect('notes')


def delete_note(request, pk):
    prod = Notes.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request,"Notes Deleted Successfuly.")
    return redirect('notes')



