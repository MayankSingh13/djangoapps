from django.shortcuts import render
from .forms import ApplyForm

# Create your views here.
def index(request):
    return render(request, "recruitment/index.html")

def apply(request):
    form = ApplyForm()
    return render(request, "recruitment/apply.html", {
        'form':form
    })
