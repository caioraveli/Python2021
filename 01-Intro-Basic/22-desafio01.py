i = 0
j = 11

for i in range(9):
    print(i,end=' ')
    j-=1
    print(j)

print()
for k,l in enumerate(range(10,1,-1)):
    print(k,l)