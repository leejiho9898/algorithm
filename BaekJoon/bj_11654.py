def ascii(text) :
    if type(text) == str:
        print(ord(text))
    else:
        print(chr(text))

K = input()

ascii(K)