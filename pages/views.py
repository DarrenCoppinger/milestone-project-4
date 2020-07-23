from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings


def contact(request):
    """"
    Returns contact form page
    """

    if request.user.is_authenticated:
        user_data = {
            'username': request.user.username,
            'email': request.user.email
        }

        contact_form = ContactForm(initial=user_data)
    else:
        contact_form = ContactForm()

    emailjs_user = settings.EMAILJS_USER

    return render(
        request,
        'contact.html',
        {'contact_form': contact_form, 'emailjs_user': emailjs_user})


def contact_success(request):
    messages.success(
        request,
        "Thank you for your message, we will be in touch shortly!")
    return redirect(reverse('index'))


def contact_error(request):
    messages.error(
        request,
        "Unable to send message, please try again")
    return redirect(reverse('contact'))


def about(request):
    return render(request, 'about.html')
