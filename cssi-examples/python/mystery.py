for i in range(1, 11):
    print(i)

def mystery1(a):
    return a + 5

def mystery2(b):
    return b * 2

result = mystery1(mystery2(3))
print(result)

def mystery(word, number):
    number = number * 2 #number is "HeHe"
    word = word.upper() # "2" is "2"
    return word * number # "2" times "HeHe" = error bc string times string is error

mystery("2", "He")
