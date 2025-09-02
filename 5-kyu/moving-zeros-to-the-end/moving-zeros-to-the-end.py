def move_zeros(lst):
    
    lst2 = []
​
    zeros = 0
    for l in lst:
        if (l != 0):
            lst2.append(l)
        else:
            zeros += 1
            
    while zeros >= 1:
        lst2.append(0)
        zeros -= 1
        
    return lst2