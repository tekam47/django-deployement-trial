from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text':'Hello World','number':100}
    return render(request,'app1/index.html',context)

def other(request):
    return render(request,'app1/other.html')

def relative(request):
    return render(request,'app1/relative_url_templates.html')