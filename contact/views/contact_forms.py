from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    if request.method == 'POST':

        context = {
            'form': ContactForm(request.POST)
        }
        return render(request, 'contact/create.html', context)