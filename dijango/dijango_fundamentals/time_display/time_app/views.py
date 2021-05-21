from django.shortcuts import render,HttpResponse
from time import gmtime, strftime, strptime

def index(request):
    context= {
        "day":strftime("%b %d, %Y", gmtime()),
        "time":strftime(" %I:%M %p", gmtime())
    }
    return render(request,'index.html',context)
    # return HttpResponse("test")