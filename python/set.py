a={6,3,8,10,15,9,2}
b={}
c={2,4,8,14,9,12}
print("a=",a)
print(type(a))
a.add(9)
print("a=",a)
print("length=",len(a))
print("max=",max(a))
print("min=",min(a))
print("sum=",sum(a))
print("sort=",sorted(a))
enum1=enumerate(a)
print(list(enum1))
print(any(b))
print(all(a))
a.remove(9)
print("a=",a)
a.pop()
print("a=",a)
set=a.union(c)
print("set=",set)
a.update(c)
print("a=",a)



