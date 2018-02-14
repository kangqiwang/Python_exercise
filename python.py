s1="   sujil      is coding   "
s1=s1.strip()
a=list(s1)
print(a)
for i in range(len(a)-1,0,-1):
	print("do something",a[i])
	if a[i]==" ":
		del a[i]
		break
	else:
		print("delete")
		del a[i]
print (a)