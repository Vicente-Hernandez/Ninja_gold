from django.shortcuts import render, redirect, HttpResponse
import random


# Create your views here

def home(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if 'messages' not in request.session:
        request.session['messages'] = []

    context = {
        'gold': request.session['gold']
    }

    return render(request, 'home.html', context)


def process_money(request, place):
    print(place)
    if place == "Granja":
        new_gold = random.randint(10, 20)
        message = f'Ganaste {new_gold} en la Granja'
        
    elif place == "Caverna":
        new_gold = random.randint(5, 10)
        message = f'Ganaste {new_gold} en la Caverna'
        
    elif place == "Casa":
        new_gold = random.randint(3, 5)
        message = f'Ganaste {new_gold} en la Casa'
        
    elif place == "Casino":
        new_gold = random.randint(-50, 50)
        if new_gold >= 0:
            message = f'Ganaste {new_gold} en el Casino'
        else:
            message = f'Perdiste {new_gold} en el Casino'

    request.session["gold"] += new_gold
    request.session['messages'].append(message)

    #if new_gold > 0:
        #request.session["activities"].append({
            #'text': f"Haz ganado {new_gold} oros en el/la {place}",
            #'gold': new_gold
        #})
    
    #else:
        #request.session["activities"].append({
            #'text': f'Haz perdido {new_gold} oros en el Casino',
            #'gold': new_gold
        #})

    return redirect("/ninja_gold")


def reset(request):
    request.session['gold'] = 0
    request.session['messages'] = []
    return redirect("/ninja_gold")
