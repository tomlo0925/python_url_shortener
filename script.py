convStr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def shortener(id):
    id = int(id)
    shortURL = ''
    while id:
        index = id % 62
        shortURL += convStr[index] 
        id = int(id / 62)

    return shortURL[::-1]


def reverse(shortURL):
    id = 0
    temp_url = shortURL[::-1]
    for i in range(len(temp_url)):
        character = temp_url[i]
        index = convStr.index(character)
        id += index*(62**i) 
    return id