a=[1,3.2,4]
b=[5,6]
print("a= ",a)
print("a= ",a[1])
print("length",len(a))
a.append(2)
print("a= ",a)
a.extend(b)
print("new= ",a)
print(max(a))
print(min(a))
print(a.count(5))
print(a.index(1))
a.insert(3,5)
print("a= ",a)
a.sort()
print("a= ",a)
a.pop(1)
print(a)
#a.clear()
c=a.copy()
print("c=",c)
print(type(a))
