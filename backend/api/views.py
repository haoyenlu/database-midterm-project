from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Type,Spot,Surfshop,News,Information,Reviewer,Recommendation,Town

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
            return Response("Some parameter is missing. required(City,Town,Beach,Date,Time)",status=status.HTTP_400_BAD_REQUEST)
        
        town_id = Town.objects.filter(city=city,name=town).values('id')
        beaches = list(Spot.objects.filter(town_id=town_id).values('name','lon','lat'))
        return Response(beaches,status=status.HTTP_200_OK)

        
@api_view(['POST'])
def beach_information(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.",status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            beach_name = request.data['beach']
            date = request.data['date']
            time = request.data['time']
        except:
            return Response("Some parameter is missing. required(Beach)",status=status.HTTP_400_BAD_REQUEST)
        
        spot_id = Spot.objects.get(name=beach_name).id
        surfshops = list(Surfshop.objects.filter(spot=spot_id).values('name','address','rating','operating_now'))
        news = list(News.objects.filter(spot=spot_id).values('date','url','title'))
        information = list(Information.objects.filter(spot=spot_id).values('date','wave_height','wave_period','wave_direction','wind_speed','wind_direction','temperature','sea_temperature','score'))
        recommendations = list(Recommendation.objects.filter(spot=spot_id).values('reviewer','score','cotent','date'))
        for recommendation in recommendations:
            reviewer = Reviewer.objects.get(id=recommendation.reviewer).values('name','email')
            recommendation['reviewer'] = reviewer
        
        response_data = {}
        response_data['surfshop'] = surfshop
        response_data['news'] = news
        response_data['information'] = information
        response_data['recommendation'] = recommendations

        return Response(response_data,status=status.HTTP_200_OK)








