from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .algorithm import encode, decode, get_all, get_all_inp, get_all_out, get_all_status, lz78_decode, lz78_encode

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

@api_view(['POST'])
def lz78_encode_view(request):
    plain_text = request.data.get('text')
    lz78_encoded_result = lz78_encode(plain_text)
    return Response({'lz78_encoded_result': lz78_encoded_result})

@api_view(['POST'])
def lz78_decode_view(request):
    compressed_data = request.data.get('text')
    lz78_decoded_result = lz78_decode(compressed_data)
    return Response({'lz78_decoded_result': lz78_decoded_result})

@api_view(['GET'])
def get_all_view(request):
    arr = get_all()
    return Response({'data' : arr})

@api_view(['GET'])
def get_all_inp_view(request):
    arr = get_all_inp()
    return Response({'data' : arr})

@api_view(['GET'])
def get_all_out_view(request):
    arr = get_all_out()
    return Response({'data' : arr})

@api_view(['GET'])
def get_all_status_view(request):
    arr = get_all_status()
    return Response({'data' : arr})