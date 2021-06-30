import io
from django.shortcuts import render
from .forms import BioForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import biodata
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# Create your views here.
def index(request):
    if request.method == "POST":
        form = BioForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            bio = biodata(first_name=first_name)
            bio.last_name = form.cleaned_data.get('last_name')
            bio.contact = form.cleaned_data.get('contact')
            bio.email = form.cleaned_data.get('email')
            bio.address = form.cleaned_data.get('address')
            bio.city = form.cleaned_data.get('city')
            bio.state = form.cleaned_data.get('state')
            bio.pincode = form.cleaned_data.get('pincode')
            bio.gender = form.cleaned_data.get('gender')
            bio.education = form.cleaned_data.get('education')
            bio.save()
            return render(request, "createbio/report.html", {
                'messages':'Registered successfully. Please generate report.',
            })
        else:
            form.errors()
            return HttpResponseRedirect(reverse("createbio:index"))
    else:
        form = BioForm()
        return render(request, "createbio/input.html", {
            'form':form
        })

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)

    bio = biodata.objects.get(id=1)

    p.setFont("Helvetica", 16)
    p.drawString(267, 820, "Biodata")
    p.line(0,818,595,818)
    p.setTitle('Your Biodata')

    #fill with database data.
    p.setFont("Times-Bold", 12)
    p.drawString(25,800, "Name: ")
    p.drawString(25,780, "Mobile: ")
    p.drawString(25,760, "Email: ")
    p.drawString(25,740, "Gender: ")
    p.drawString(25,720, "Address: ")
    p.drawString(25,700, "City: ")
    p.drawString(25,680, "State: ")
    p.drawString(25,660, "Pincode: ")
    p.drawString(25,640, "Education: ")
    p.setFont("Helvetica", 12)
    p.drawString(60,800, bio.first_name + " " + bio.last_name)
    p.drawString(66,780, str(bio.contact))
    p.drawString(62,760, bio.email)
    p.drawString(72,740, bio.gender)
    p.drawString(72,720, bio.address)
    p.drawString(62,700, bio.city)
    p.drawString(62,680, bio.state)
    p.drawString(70,660, str(bio.pincode))
    p.drawString(82,640, bio.education)
    p.drawString(286,10, str(p.getPageNumber()))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def report(request):
    return render(request, "createbio/report.html")
