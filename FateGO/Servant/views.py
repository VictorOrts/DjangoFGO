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
    for i in servant:
        b = 0
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
        # Code to avoid className beast not servants
        positionbeast = meal_data.className.find("beast")
        meal_data.save() if positionbeast < b else meal_data.delete()
        all_meals = Servantch.objects.all()

    all_meals.order_by('-collectionNo')
    
    return render (request, 'main.html', { "all_meals": 
    all_meals} )