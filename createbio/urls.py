from django.urls import path

from . import views

app_name = "createbio"
urlpatterns = [
    path("", views.index, name="index"),
    path("report", views.report, name="report"),
    path("generate_pdf", views.generate_pdf, name="generate_pdf"),
]
