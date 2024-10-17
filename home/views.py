from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Image
from django.db.models import Q

# Create your views here.
def index(request):
    obj=Image.objects.all()
    return render(request, 'home/index.html',{'image':obj})

def detail_view(request, id, slug):
    obj=get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'home/detail.html',{'image':obj})

def search(request):
    query=None
    result=[]
    if request.method == 'GET' :
        query=request.GET.get('search')
        result=Image.objects.filter(Q(title__icontains=query) | Q(sname__icontains=query) | Q(tags__icontains=query)
                                    | Q(sdesc__icontains=query) | Q(ldesc__icontains=query))
    return render(request, 'home/search.html',{'query':query, 'result':result})