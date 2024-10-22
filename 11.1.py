t=(1,2,3,4)
t1=(3,5,2,1)
t2=(2,2,3,1)

print(t,t1,t2)


print(tuple(map(sum,zip(t,t1,t2))))
