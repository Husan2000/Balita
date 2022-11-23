from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from about.models import About


def contact_view(request):
    objects = About.objects.order_by('-id')[:3]
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'successfully send your message')
        return redirect('#contact/')
    context = {
        'form': form,
        'objects': objects,
    }
    return render(request, 'contact/index.html', context)
