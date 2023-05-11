print("hello world")


a=10
print(type(a))

a=["asa",9,9.0]
print(a)
print(type(a))
print(a[0])
a[0]="anna"
print(a)
a.append(50)
print(a)

a,b,c=10,10.0,"dsad"
print(a,b,c)
print(type(a),type(b),type(c))


a=b=c=10
print(a,b,c)

a='xsc'
b="sc"
print(type(a),type(b))


v=("xxcx",9.0,8,9,0)
print(v)
print(type(v))


s={9,8,7,9,8,7,"dtfd",9.0}
print(s)
print(type(s))


n={"no":1,"name":"anna"}
print(n)
print(type(n))


a=5
b=5
if a>b:
	print('a is grater')
elif a==b:
	print('the values equal')
else:
	print('b is grater')
	

a=10
b=9
c=8
if a>b and a>c:
	print("a is grater",a)
elif b>a and b>c:
	print("b is grater",b)
else:
	print("c is grater",c)


for i in range(5,10):
	print(i)

i=0
while(i<100):
	print(i)
	i+=3

for i in range(0,10):
	print(" "*(10-i),end="")
	print(" *"*i)

for x in 'bananana':
	print(x)
