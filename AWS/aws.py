def solution(T,R):
    temp_success = []
    temp_elim = []
    pos,val = find_number(T[0])
    groups = set()
    for j in T:
        groups.add(j[pos])
    groups = list(sorted(groups))
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
            if g in test and R[k] == 'OK':
                possible_success.append(g)
    return possible_success


def find_number(v):
    for k,v in enumerate(v):
        if v.isnumeric():
            return k,v

def success(allgrp,success):
    return (success *100 )/allgrp

tests = ['test1a','test2','test1b','test1c','test3','test4','test5','test6','test7','test8','test9','test10','test11','test12','test11a']
results = ['Wrong Answer','OK','Runtime error','OK','Time limit exceeded','Time limit exceeded','OK','Runtime error','OK','Runtime error','OK','Wrong Answer','OK','Wrong Answer','OK']


print(len(tests),len(results))
print(solution(tests,results))

test2 = ['codility1','codility3','codility2','codility4b','codility4a']
results2 = ['Wrong Answer','OK','OK','Runtime error','OK']

print(solution(test2,results2))