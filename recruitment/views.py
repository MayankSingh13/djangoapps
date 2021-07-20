from django.shortcuts import render
from .forms import ApplyForm
from .models import PersonalDetails
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "recruitment/index.html")

def apply(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            max_id = PersonalDetails.objects.all().aggregate(Max('id'))
            if max_id['id__max'] == None:
                max_id['id__max'] = 1
                applicant_id = 2021220000 + max_id['id__max']
            else:
                max_id = PersonalDetails.objects.all().aggregate(Max('applicant_id'))
                applicant_id = applicant_id + max_id['applicant_id__max']
            print(applicant_id)
            applicant = PersonalDetails(applicant_id=applicant_id)
            applicant.full_name = form.cleaned_data.get('full_name')
            applicant.parent_name = form.cleaned_data.get('parent_name')
            applicant.dob = form.cleaned_data.get('dob')
            applicant.gender = form.cleaned_data.get('gender')
            applicant.category = form.cleaned_data.get('category')
            applicant.mob_no = form.cleaned_data.get('mob_no')
            applicant.email = form.cleaned_data.get('email')
            applicant.nationality = form.cleaned_data.get('nationality')
            applicant.save()
            messages.success(request, 'Registered successfully. Please go to login page.')
            return HttpResponseRedirect(reverse("recruitment:apply"))
        else:
            print(form.errors)
    else:
        form = ApplyForm()
        return render(request, "recruitment/apply.html", {
            'form':form
        })
