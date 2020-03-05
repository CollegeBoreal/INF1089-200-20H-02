# -*- coding: utf-8 -*-
a=[x for x in range(0,10)]
print(a)

s=[x for x in range(10) if x%2!=0]
print(s)
#packing
a,b,c=(8,5,1)
print(a)
print(b)
print(c)
#unpacking
l=[1,2,3,45,6]
h,*t=l
print(h)
print(t)
head,*trail=[x for x in range(10)]
print(head)
print(trail)
f=lambda x:x+3
print(f(3))

g=lambda x, y: x+y
print(g(1,2))

p=lambda a:a
print(p(4))