from django.shortcuts import render, get_object_or_404
from . models import Dino


def show_all_dinos(request):
    dinos = Dino.objects.all()
    for dino in dinos:
        dino.save()
    return render(request, 'dino_app/all_dinos.html', {
        'dinos': dinos
    })


def show_one_dino(request, slug_dino: str):
    dino = get_object_or_404(Dino, slug=slug_dino)
    return render(request, 'dino_app/one_dino.html', {
        'dino': dino
    })