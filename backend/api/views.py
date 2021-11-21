from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Type,Spot,Surfshop,News,Information,Reviewer,Recommend,Town

# Create your views here.

@api_view(['GET','POST'])
def town_list(request):
    if request.method == 'GET':
        town = list(Town.objects.values_list('city').distinct());
        return Response(town,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        try:
            city = request.data['city']
        except:
            return Response("Some parameter is missing. required(city)",status=status.HTTP_400_BAD_REQUEST)
        town = list(Town.objects.filter(city=city).values_list('name'))
        return Response(town,status=status.HTTP_200_OK)


@api_view(['POST'])
def beach_search(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.",status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            city = request.data['city']
            town = request.data['town']
        except:
            return Response("Some parameter is missing. required(city,town)",status=status.HTTP_400_BAD_REQUEST)
        
        
        town_id = Town.objects.filter(city=city,name=town).values('id')[0]['id']
        beaches = list(Spot.objects.filter(town_id=town_id).values('name','lon','lat'))

        for beach in beaches:
            beach_type_id = Spot.objects.filter(name=beach["name"]).values('type')[0]['type']
            beach_type = Type.objects.get(id=beach_type_id).name
            beach["type"] = beach_type

        return Response(beaches,status=status.HTTP_200_OK)

        
@api_view(['POST'])
def beach_information(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.",status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            beach_name = request.data['beach']
        except:
            return Response("Some parameter is missing. required(Beach)",status=status.HTTP_400_BAD_REQUEST)
        
        _spot = Spot.objects.get(name=beach_name)
        spot_id = _spot.id
        beach_type = _spot.type
        

        surfshops = list(Surfshop.objects.filter(spot=spot_id).values('name','address','rating','operating_now'))
        news = list(News.objects.filter(spot=spot_id).values('date','url','title'))
        information = list(Information.objects.filter(spot=spot_id).values('date','wave_height','wave_period','wave_direction','wind_speed','wind_direction','temperature','sea_temperature','score'))
        recommendations = Recommend.objects.filter(spot=spot_id).values('reviewer','score','content','date')
        for recommendation in recommendations:
            reviewer = Reviewer.objects.get(id=recommendation['reviewer'])
            recommendation['reviewer'] = {"name":reviewer.name,"email":reviewer.email}
        
        response_data = {}
        response_data['surfshop'] = surfshops
        response_data['news'] = news
        response_data['information'] = information
        response_data['recommendation'] = recommendations
        response_data['type'] = beach_type.name

        return Response(response_data,status=status.HTTP_200_OK)








