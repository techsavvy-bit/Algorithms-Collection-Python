import bisect

def previous_intervals(I):
    start = [task[0] for task in I]
    finish = [task[1] for task in I]
    p = []
    
    for i in range(len(I)):
        # finds idx for which to input start[i] in finish times to still be sorted
        idx = bisect.bisect(finish, start[i]) - 1
        p.append(idx)

    return p
    
def compute_opt(j):
    if j == -1:
        return 0
    
    elif (0 <= j) and (j < len(OPT)):
        return OPT[j]
    else:
        return max(I[j][2] + compute_opt(p[j]), compute_opt(j-1))

def find_solution(j):
    if j == -1:
        return
    else:
        if (I[j][2] + OPT[p[j]]) >= OPT[j-1]:
            O.append(I[j])
            find_solution(p[j])
            
        else:
            find_solution(j-1)

def weighted_interval(I):
    for j in range(len(I)):
        opt_j = compute_opt(j)
        OPT.append(opt_j)
    
    find_solution(len(I) - 1)

    return OPT[-1], O
    

if __name__ == '__main__':
    OPT = []
    O   = []
    # They are labeled as:  (start, end, weight)
    t1 = (0,4,2)
    t2 = (1,6,4)
    t3 = (5,7,4)
    t4 = (3,9,7)
    t5 = (8,10,2)
    t6 = (8,11,1)
    I = [t1,t2,t3,t4,t5,t6]
    
    I.sort(key = lambda tup : tup[1])
    p = previous_intervals(I)
    
    max_weight, solution = weighted_interval(I)
