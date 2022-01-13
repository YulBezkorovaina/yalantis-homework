 #!venv/bin/python

if __name__ == "__main__":
    print("Hello, I am program!")
    a = 1
    print(dir(a))

    #methods STR
    S = "Hello my teacher!"
    print(S.isupper())
    S1 = S.upper()
    print(S1.isupper())
    print(S)
    print(S.find("my"))
    print(S.split(" "))

    #methods dict
    d = {'d' : 1, 'b' : 2, 'a' : 3}
    print(d)
    print(d.get('a'))
    print(d['b'])
    print(d.keys())

    #methods list
    l = ['abc', 'def', '123', '456', 'ad1', 'be4']
    print(l)
    l.pop(1)
    print(l)
    l.sort()
    print(l)
    l.reverse()
    print(l)






