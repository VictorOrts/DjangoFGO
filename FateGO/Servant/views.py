from django.shortcuts import render
from .models import Servantch
import requests
# Create your views here.


def Servant(request):
    all_meals = {}
    url = 'https://api.atlasacademy.io/export/NA/basic_servant.json'
    response = requests.get(url)
    data = response.json()
    servant = data
    print(servant)
    for i in servant:
        meal_data = Servantch(
            unique_id  = i['id'],
            collectionNo = i['collectionNo'],
            name = i['name'],
            typeS = i['type'],
            flag = i['flag'],
            className = i['className'],
            attribute = i['attribute'],
            rarity = i['rarity'],
            atkMax = i['atkMax'],
            hpMax = i['hpMax'],
            face = i['face']
        )
        meal_data.save()
        all_meals = Servantch.objects.all().order_by('collectionNo')

    return render (request, 'main.html', { "all_meals": 
    all_meals} )