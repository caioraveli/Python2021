def solution(A):
    # write your code in Python 3.6
    #smaller = sorted(list(set(A)))
    #last_number = smaller[-1]
    #if last_number < 0:
    #    return 1
    #else:
    #    new_smaller = [ x for x in smaller if x > 0 ]
    #    for num in new_smaller:
    #        if num not in new_smaller:
    #            return num

    #num = 1
    s = sorted(list(set(A)))
    new_smaller = [ x for x in s if x > 0 ]
    for num in range(1,len(new_smaller)):
        if num not in new_smaller:
            return num
        

b = [-1,-2,-3,-1,-2,1,2,3,4,5,20,30]

print(solution(b))


#a = [0,-5,6,7,9,20,1,8,10]

#small = sorted(list(set(a)))
#print(small[-1])