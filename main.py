 #!venv/bin/python

if __name__ == "__main__":
    print("Hello, I am program!")
    a = 1
    print(dir(a))

    #methods STR
    S:str; S = "Hello my teacher!"
    print(S.isupper())
    S1 : str = S.upper()
    print(S1.isupper())
    print(S)
    print(S.find("my"))
    print(S.split(" "))

    #methods dict lesson_1_taks
    d : dict = {'d' : 1, 'b' : 2, 'a' : 3}
    print(d)
    print(d.get('a'))
    print(d['b'])
    print(d.keys())

    #methods list  lesson_1_taks
    l : list = ['abc', 'def', '123', '456', 'ad1', 'be4']
    print(l)
    l.pop(1)
    print(l)
    l.sort()
    print(l)
    l.reverse()
    print(l)

    #methods set  lesson_1
    s : set = set(S)
    print(s)
    print(len(s))
    s1 : set = set("abcdef")
    print(s1)
    s2 : set = s.union(s1)
    print(s2)

    #methods tuple  lesson_1
    t : tuple = s2
    print(t)
    print(t.intersection('e'))
    t1 = tuple("aqwasetghj")
    print(t1)






