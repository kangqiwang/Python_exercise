s1="sujil is coding"
a=list(s1)
print(a)
for i in range(len(a)-1,0,-1):
	print("do something")
	if a[i]==" ":
		del a[i]
		break
	else:
		print("delete")
		del a[i]
print (a)

