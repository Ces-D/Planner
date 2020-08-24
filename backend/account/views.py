from django.shortcuts import render

from rest_framework import status, generics

from .models import User
from .serializers import UserCreateSerializer