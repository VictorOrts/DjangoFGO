from django.shortcuts import render,redirect
from .models import Servantch
import datetime
from django.http import HttpResponse
import requests
# Create your views here.

async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)


     


def Servant(request):
    servantfilter = request.GET.get('servant')
    print(servantfilter)
    mainurl=""
    if servantfilter:
        print(servantfilter)
        url2 = 'https://api.atlasacademy.io/basic/NA/servant/search?lang=en&name='+servantfilter
        mainurl = url2
    else:
        url = 'https://api.atlasacademy.io/export/NA/basic_servant.json'
        mainurl = url

    all_meals = []
    response = requests.get(mainurl)
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
        namefilter = meal_data.name.find("servantfilter")
        meal_data.save() if namefilter < b else meal_data.delete()
        all_meals.append(meal_data)

    #all_meals.order_by('-collectionNo')
    return render (request, 'main.html', { "all_meals": 
    all_meals} )

def informationCharacter(request,collectionNo):
   print("Info character")
   url = 'https://api.atlasacademy.io/basic/NA/servant/'+str(collectionNo)
   return redirect(url)

