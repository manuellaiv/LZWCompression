def lz78_encode(plain):
    i = 0
    compressed = []
    entry = ['']
    while i < len(plain):
        check = plain[i]
        if not (check in compressed):
            entry.append(check)
            compressed.append('0')
            compressed.append(check)
            i = i + 1
        else:
            while(i < len(plain)) and (check in entry):
                if (i == len(plain)-1 or not (check + plain[i+1] in entry)):
                    break
                i = i + 1
                check = check + plain[i]
            if i == len(plain)-1:
                compressed.append(str(entry.index(check)))
                compressed.append('xx')
                i = i + 1
            else:
                compressed.append(str(entry.index(check)))
                i = i + 1
                check = check + plain[i]
                compressed.append(plain[i])
                entry.append(check)
                i = i + 1
    compressed_str = ""
    for i in range(len(compressed)):
        if i == len(compressed)-1:
            compressed_str = compressed_str + compressed[i]
        else:
            compressed_str = compressed_str + compressed[i] + ","
    return compressed_str

def lz78_decode(compr):
    compressed = compr.split(',')
    plain = ""
    entry = ['']

    for i in range(0, len(compressed), 2):
        idx = int(compressed[i])
        el = (compressed[i+1])

        if el == "xx":
            plain = plain + entry[idx]
        elif idx == 0:
            plain = plain + el
            entry.append(el)
        else:
            entry.append(entry[idx] + el)
            plain = plain + entry[idx] + el
    return plain