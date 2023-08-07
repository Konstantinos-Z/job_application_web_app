from django.shortcuts import render
from .forms import ApplicationForm, EnquiryForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            message_body = f"""A new job application was submitted. Thank you, {first_name}.
            here are the submitted data:
            Name: {first_name} {last_name}
            Start date: {date}
            Email: {email}
            Current occupation: {occupation}
            """
            email_message = EmailMessage("Form submission confirmation",
                                         message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            enquiry = form.cleaned_data["enquiry"]

            message_body = f"Enquiry: {enquiry}\nContact Email: {email}"
            email_message = EmailMessage(f"New enquiry by {email}", message_body,
                                         to=["zigouris.konstantinos@gmail.com"])
            email_message.send()

            messages.success(request, "Enquiry submitted successfully!")
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
