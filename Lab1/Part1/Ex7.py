x = 'spam'
while x: # while x is not empty
	print(x,end=' ') # in 2.X use print x
	x=x[1:] # strip first character off x
a=0; b=10
while a<b: # one way to code counter loops
	print(a,end=' ')
	a+=1 # or, a = a + 1
x=10
while x:
	x=x-1 # or, x -=1
	if x%2 !=0: continue # odd? – skip print
	print(x, end=' ')
for x in ["spam", "eggs", "ham"]:
	print(x, end=' ')
sum = 0
for x in [1, 2, 3, 4]:
	sum = sum + x
sum
prod = 1
for item in [1,2,3,4]: prod*= item
prod
