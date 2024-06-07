from .serializer import FoodSerializer
from rest_framework.response import Response 
from rest_framework.views import  status
from rest_framework.decorators import api_view
from .models import Foods




@api_view(["GET", "POST"])
def FoodViews(request):
    
    if request.method == "GET":
        food = Foods.objects.all()
        srlz = FoodSerializer(food, many=True)
        return Response(srlz.data)

    if request.method == "POST":
        food_serializer = FoodSerializer(data = request.data)
        if food_serializer.is_valid():
            food_serializer.save()
            return Response({"Mensaje":"Food add successfully"},
                             status=status.HTTP_201_CREATED)
        else:
             return Response({"Mensaje":"Error add Food"},
                              status=status.HTTP_401_UNAUTHORIZED)