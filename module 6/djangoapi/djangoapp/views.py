from django.shortcuts import render
from .models import Book_model
from .serializers import Book_serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def displaydata (request):

    userdata = Book_model.objects.all()
    try :
        userserializer = Book_serializers(userdata,many=True)
        return Response (userserializer.data)
    except Exception as e :
        print (e)

# Crud Opertions in Django Restframework

@api_view(['POST'])
def insertdata (request):

    if request.method == 'POST':
        userserializer = Book_serializers(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response (status=status.HTTP_204_NO_CONTENT)
    
    return Response (status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def fetchdata (request,id):

    userdata = Book_model.objects.get(id=id)
    try :
        userserializer = Book_serializers(userdata)
    except Exception as e :
        print (e)
    
    return Response (userserializer.data)
    

@api_view(['GET','DELETE'])
def deletedata (request,id):
    userdata = Book_model.objects.get(id=id)

    if request.method == 'GET':
        userdataserializer = Book_serializers(userdata)
        return Response (userdataserializer.data)
    
    if request.method == 'DELETE':
        try :
            userserializer = Book_serializers(userdata)
            if userserializer.is_valid():
                userdata.delete()
                return Response (status=status.HTTP_202_ACCEPTED)
        except Exception as e :
            print (e)

    return Response (status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET','PUT'])
def updatedata (request,id):

    userdata = Book_model.objects.get(id=id)

    if request.method == 'GET':
        userdataserializer = Book_serializers(userdata)
        return Response (userdataserializer.data)
    
    if request.method == 'PUT':
        try :
            userserializer = Book_serializers(data=request.data,instance=userdata)
            if userserializer.is_valid():
                userserializer.save()
                return Response (status=status.HTTP_202_ACCEPTED)
        except Exception as e :
            print (e)

    return Response (status=status.HTTP_404_NOT_FOUND)

