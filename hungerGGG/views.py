from django.http import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from .forms import TributeForm
from .models import Game_session

def home(request):
    if request.method == 'POST':

        tributes_list = []
    
        for form_n in range(len( request.POST.getlist('name') )) :

            #try:
            tribute = {}
            tribute['name'] = request.POST.getlist('name')[form_n]
            tribute['nature'] = request.POST.getlist('nature')[form_n]
            tribute['is_alive'] = True
            tribute['district'] = request.POST.getlist('district')[form_n]

            tributes_list.append(tribute)
                
            #except:
            #    return render(request, 'hungerGGG/home.html')
        
        game_session = Game_session.objects.create()
        game_session.tributes = str(tributes_list)

        game_session.save()

        return redirect('game', id = game_session.pk)

    else:
        return render(request, 'hungerGGG/home.html')

def tribute_forms(request):

    forms = []

    for x in range(int(request.POST['tributes'])):
        form_created = TributeForm()
        forms.append(form_created)

    html = render(request, 'hungerGGG/tribute-forms.html', {'forms' : forms})

    return HttpResponse(html)

def game(request, id):
    
    return render(request, 'hungerGGG/game.html')