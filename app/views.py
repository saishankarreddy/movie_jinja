from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':"pushpa",'age':22}
    return render(request,'p.html',context=d)
