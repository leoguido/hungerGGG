from django.shortcuts import render, HttpResponse
from .forms import TributeForm

def home(request):

    return render(request, 'hungerGGG/home.html')

def tribute_forms(request):

    forms = []

    for x in range(int(request.POST['tributes'])):
        form_created = TributeForm()
        forms.append(form_created)

    html = render(request, 'hungerGGG/tribute-forms.html', {'forms' : forms})

    return HttpResponse(html)