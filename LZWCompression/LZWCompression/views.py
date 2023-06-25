from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .algorithm import encode, decode

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def encode_view(request):
    plain_text = request.data.get('text')
    encoded_result = encode(plain_text)
    return Response({'encoded_result': encoded_result})

@api_view(['POST'])
def decode_view(request):
    compressed_data = request.data.get('text')
    decoded_result = decode(compressed_data)
    return Response({'decoded_result': decoded_result})