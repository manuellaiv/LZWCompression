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

    return result

def decode(compr):
    # Initial dictionary
    dictionary = {}
    for i in range(256):
        dictionary[i] = chr(i)

    # Algorithm
    check = ""
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

    return plain