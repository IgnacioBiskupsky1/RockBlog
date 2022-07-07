from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from blog.models import BlogPost
from rest_noticia.serializers import BlogPostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_noticias(request):
    if request.method == 'GET':
        listaNoticias = BlogPost.objects.all()
        serializer = BlogPostSerializer(listaNoticias, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = BlogPostSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
        
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_noticia(request, id):
    try:
        noticia = BlogPost.objects.get(title=id)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogPostSerializer(noticia)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = BlogPostSerializer(noticia, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        noticia.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)











