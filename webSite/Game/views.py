from django.shortcuts import render
from .models import Character_class,Character

# Create your views here.
def Game(request):
    Char_class = Character_class.objects.all()
    Char = Character.objects.all()
    context = {
        'Char_class': Char_class,
        'Char': Char
    }
    return render(request, 'main.html', context)