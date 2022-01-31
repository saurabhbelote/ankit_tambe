from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewUserSerializer
from .models import NewUser
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = NewUserSerializer
    queryset = NewUser.objects.all()
    def list(self, request):
        queryset = self.get_queryset()
        serializer = NewUserSerializer(queryset, many=True)
        return Response(serializer.data)