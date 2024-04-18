def fun(key, value):
    str1 = format(key, str(value))
    return str1

dict = {'a':10, 'b':12, 'c':13, 'd':14}
itar = map(fun, dict)
t = tuple(itar)
print(t)


