from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:index')

        return render(request, 'contact/create.html', context)