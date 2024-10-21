t1=(1,2,3,4)
t2=(3,5,2)
t3=(2,2,3,1)
print(t1,t2,t3)

res=tuple(map(sum,zip(t1,t2,t3)))
print(res)