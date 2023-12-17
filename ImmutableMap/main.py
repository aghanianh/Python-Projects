from immutablemap import ImmutableMap

proxy = ImmutableMap({'a':1, "b":2}, c = 3, d = 4)
proxy1 = ImmutableMap(a = 1, b = 2, c = 3, d = 4)
proxy2 = ImmutableMap(d = 5, e = 6, f = 7, g = 8)
ordinary = dict(a = 1, b = 2, c = 3, d = 4)
print("proxy: ", proxy)
print("proxy1: ", proxy1)
print("proxy2: ", proxy2)
print("Length of proxy is ", proxy.__len__())
print("is 'a' in proxy :", proxy.__contains__('a'))
#print("proxy == ordinar:", proxy == ordinary)
#proxy.__delitem__('a')
print("is proxy == proxy2:", proxy == proxy2)

for key, value in proxy.items():
    print("key:", key, "value: ", value)


proxy.pop('a')


