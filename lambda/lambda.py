l0=2000
list1=[]
for n in range(1,10):
    for m in range(1,10):
        if n!=m:
            l=l0/(n**2-m**2)
            list1.append(l)
flist=filter(lambda x:x>=380 and x<=740,list1)
print(list(flist))