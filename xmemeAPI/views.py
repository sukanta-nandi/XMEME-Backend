from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import memeData
from .serializers import memeDataSerializer
from django.http import Http404

# Create your views here.


class memeAPI(APIView):
    """APIView for memeData """


    def get(self, request, pk=None, format=None):
        """Returns list or specific memes data """
        memeId = pk
        if memeId is not None:
            try:
                meme = memeData.objects.get(id=memeId)
                print(meme)
                serializer = memeDataSerializer(meme)
                return Response(serializer.data)
            except memeData.DoesNotExist:
                raise Http404
        else:
            memes = memeData.objects.all().order_by('-id')
            serializer = memeDataSerializer(memes, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        """Creates a new meme object and serializes"""
        serializer = memeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id' : serializer.data['id']}, 
                             status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        """Updates a meme instace completely"""
        memeId = pk
        meme = memeData.objects.get(pk=memeId)
        serializer = memeDataSerializer(meme, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Your request has been updated successfully : PUT'})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """Updates a meme instace partially"""
        memeId = pk
        meme = memeData.objects.get(pk=memeId)
        serializer = memeDataSerializer(meme, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Your request has been updated : PATCH'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        """Deletes a meme instace"""
        memeId = pk
        meme = memeData.objects.get(pk=memeId)
        meme.delete()
        return Response({'msg': 'Successfully deleted requested data'})