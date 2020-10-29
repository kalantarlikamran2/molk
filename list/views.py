from django.shortcuts import render
from list.models import Telebe

# Create your views here.

def list(request):
    post = Telebe.objects.all()

    context={
        'post': post,


    }

    return render(request,'list/list.html',context)