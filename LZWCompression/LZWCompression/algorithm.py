import json
from .models import Translation

def encode(plain):
    # Initial dictionary
    dictionary = {}
    for i in range(256):
        dictionary[chr(i)] = i

    # Algorithm
    check = ""
    result = []
    for ch in plain:
        if (check + ch in dictionary):
            check = check + ch
        else:
            result.append(dictionary[check])
            dictionary[check + ch] = len(dictionary)
            check = ch

    if (check in dictionary):
        result.append(dictionary[check])

    res = ''
    for i in range(len(result)):
        if (i == len(result)-1):
            res = res + str(result[i])
        else:
            res = res + str(result[i]) + ","

    new_translation = Translation(inp = plain, out = res, status = 0)
    new_translation.save()
    return result

def decode(compr):
    # Initial dictionary
    dictionary = {}
    for i in range(256):
        dictionary[i] = chr(i)

    # Algorithm
    compressed_str = compr.split(',')
    compressed = [int(ch) for ch in compressed_str]
    plain = dictionary[compressed[0]]
    prev = plain

    for i in range(1, len(compressed)):
        current = ""

        if compressed[i] in dictionary:
            current = dictionary[compressed[i]]
        elif compressed[i] == len(dictionary):
            current = prev + prev[0]

        plain = plain + current
        dictionary[len(dictionary)] = prev + current[0]
        prev = current

    new_translation = Translation(inp = compr, out = plain, status = 1)
    new_translation.save()
    return plain

def get_all():
    arr = Translation.objects.all()
    return arr

def get_all_inp():
    inp_data = Translation.objects.values_list('inp', flat=True)
    inp_list = list(inp_data)
    return inp_list

def get_all_out():
    out_data = Translation.objects.values_list('out', flat=True)
    out_list = list(out_data)
    return out_list

def get_all_status():
    status_data = Translation.objects.values_list('status', flat=True)
    status_list = list(status_data)
    return status_list