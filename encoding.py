def encode(text, padding=0):
    array = [];
    for letter in text:
        array.append(ord(letter))
    for i in range(padding - len(text)):
        array.append(0)
    return array


def decode(array):
    output = "";
    for encoded in array:
        output += chr(encoded)
    return output
