from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.views import Type,Spot,Surfshop,News,Information,Reviewer,Recommendation,Town

# Create your views here.

@api_view(['GET','POST'])
def town_list(request):
    if request.method = 'GET':
        town = list(Town.objects.values())
        return Response(town,status=status.HTTP_200_OK)
    
    if request.method = 'POST':
        city = request.data['city']
        town = list(Town.objects.filter(city=city).values('name'))
        return Response(town,status=status.HTTP_200_OK)


@api_view(['POST'])
def beach_search(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.",status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            city = request.data['city']
            town = request.data['town']
            date = request.data['date']
            time = request.data['time']
        except:
            return Response("Some parameter is missing. required(City,Town,Beach,Date,Time)",status=status.HTTP_400_BAD_REQUEST)

    

        
@api_view(['POST'])
def beach_information(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.",status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            beach = request.data['beach']
        except:
            return Response("Some parameter is missing. required(Beach)",status=status.HTTP_400_BAD_REQUEST)


