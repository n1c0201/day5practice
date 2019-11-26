def detectvowels(char):
    vowels = ('a', 'i', 'u', 'e', 'o', ' ')
    return char.lower() in vowels
def translate(text):
    newtext = ""
    for i in text:
        if detectvowels(i):
            newtext += i
        else:
            newtext += i + "o" + i
    return newtext

print(translate("I want to game end myself"))