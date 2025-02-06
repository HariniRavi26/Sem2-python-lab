"""#lambda arguments:expression
mul= lambda a,b : a * b

print(mul(1,2))

#square each element in a list
L1=list(map(int,input().split()))
square=map(lambda x : x**2 , L1)
print(list(square))

L2=list(map(int,input().split()))
even=filter(lambda x : x%2==0 ,L2)
print(list(even)) 

t=[("harii",2),("elakiya",3),("shameera",1)]
t1=sorted(t,key=lambda x:x[1])
print(t1)

name=["hari","mithu","elaks"]
salary=[20000,50000,30000]
S=zip(name,salary)
sort=sorted(S,key=lambda k:k[1])
print(sort)"""

div=lambda a,b : a//b
print(div(10,5))

