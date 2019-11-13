def myfunc(string):
    toUpper = True
    word = []
    for character in string:
        if toUpper:
            word.append(character.upper())
        else:
             word.append(character.lower())
        toUpper = not toUpper
    return ''.join(word)

print(myfunc('hello World'))
