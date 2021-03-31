from functools import reduce
from math import floor

def solution(T,R):
    temp_success = []
    groups = find_number(T)
    itsnow = eliminate(groups,T,R)

    for m in itsnow:
        for k,n in enumerate(T):
            if m in n and R[k] != 'OK':
                break
            elif m not in n:
                continue
            else:
                temp_success.append(m)
    return success(len(groups),len(temp_success))

def eliminate(grp,T,R):
    possible_success = []
    for g in grp:
       for k,test in enumerate(T):
            g = str(g)
            if str(g) in test and R[k] == 'OK':
                possible_success.append(g)
    return possible_success


def find_number(tests):
    first_num = [ k for k,n in enumerate(tests[0]) if n.isnumeric()]
    first_num = reduce(lambda x:x,first_num)
    allNumbers= []
    groups = set()
    for j,test in enumerate(tests):
        number = f'{test[first_num]}'
        temp_num = test[first_num:]
        if len(temp_num) > 1:
            for m,n in enumerate(temp_num[1:]):
                if n.isnumeric():
                   number = number+n
            allNumbers.append(int(number))
        else:
            allNumbers.append(int(number))
    groups = set(allNumbers)
    return list(sorted(groups))

def success(allgrp,success):
    return floor((success *100 )/allgrp)

tests = ['test1a','test2','test1b','test1c','test3','test4','test5','test6','test7','test8','test9','test10','test11','test12','test11a']
results = ['Wrong Answer','OK','Runtime error','OK','Time limit exceeded','Time limit exceeded','OK','Runtime error','OK','Runtime error','OK','Wrong Answer','OK','Wrong Answer','OK']


#print(len(tests),len(results))
print(solution(tests,results))


test2 = ['codility1','codility3','codility2','codility4b','codility4a']
results2 = ['Wrong Answer','OK','OK','Runtime error','OK']

print(solution(test2,results2))