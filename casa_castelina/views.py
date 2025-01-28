import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysite import settings 
from django.contrib import messages
from django.core.mail import send_mail

# Create your views
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # COMPOSER
        subject = f"CASTELINA  Novo contato de {name}"
        email_message = f"Nome: {name}\nTelefone: {phone}\nEmail: {email}\n\nMensagem:\n {message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.CONTACT_EMAIL]
        print (f'Assunto do email: {subject}\nMensagem do Email: {email_message}\nDe: {from_email}\nA: {recipient_list}')

        # ENVIA EMAIL
        try:
            send_mail(subject, email_message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')

        return redirect('contact')
    return render(request, 'contact.html')

def galeria(request):
    return render(request, 'galeria.html')

def about(request):
    return render(request, 'about.html')
