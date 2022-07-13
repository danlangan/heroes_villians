from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        # super_types = request.query_params.get('type')
        # supers = Supers.objects.all()
        villians = Supers.objects.filter(super_type_id=2)
        heroes = Supers.objects.filter(super_type_id=1)
        hero_serializer = SupersSerializer(heroes, many=True)
        villian_serializer = SupersSerializer(villians, many=True)    
        custom_response = {
                    "heroes": hero_serializer.data,
                    "villians": villian_serializer.data
                }    
                
        return Response(custom_response)

        
            
        # else:
        #     supers = supers.filter(super_type__type=super_types)
        # serializer = SupersSerializer(supers, many=True)
        # return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def super_function_by_id(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)