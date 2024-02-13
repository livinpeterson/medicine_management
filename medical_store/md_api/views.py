from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from medicine_management.forms import Medicineform
from medicine_management.models import Medicine
from .serializers import MedicineSerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_medi(request):
    form = UserCreationForm(data = request.data)
    
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=HTTP_201_CREATED)
    return Response(form.errors, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login_medi(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username & password'}, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentinals'}, status=HTTP_404_NOT_FOUND)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_medi(request):
    medicine = Medicine.objects.all()
    serializer = MedicineSerializer(medicine, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_medi(request, name):
    medicine = Medicine.objects.filter(name__istartswith=name)
    serializer = MedicineSerializer(medicine, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_medi(request):
    form = Medicineform(request.POST)
    if form.is_valid():
        medicine = form.save()
        return Response({'id':medicine.id}, status=HTTP_201_CREATED)
    return Response(form.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_medi(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    form = Medicineform(request.POST, instance=medicine)
    if form.is_valid():
        medicine = form.save()
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_medi(request, id):
    try:
        medicine = Medicine.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    
    medicine.delete()
    return Response("Deleted Successfully")