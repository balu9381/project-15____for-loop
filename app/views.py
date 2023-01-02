from django.shortcuts import render

# Create your views here.
def ravi(request):
    d={'name':'balu','L':[1,1,1,]}
    return render(request,'balu.html',d)