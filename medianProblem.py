# x = [0,1,2,3,4,5]
# y = [6,7,8,9,10]
x = [39, 77, 45, 92, 22, 83, 40, 36, 51, 12, 66,  5, 38]
y = [16, 52, 25, 24, 47, 64, 13, 84, 79, 56, 62]
x.sort()
y.sort()

import math
import collections

def median(x,y):
    
    # z = list(set(x) | set(y))
    # z.sort()
    # if len(z)%2 == 0:
    #     result = (z[len(z)//2-1] + z[len(z)//2])/2
    # else:
    #     result = z[math.ceil(len(z)/2)-1]
    # d = collections.OrderedDict.
    d = {}
    for i in range(len(x)+len(y)):
        if i<len(x):
            d[i] = x[i]
        if i<len(y):
            d[i+1] = y[i]
        # for i in x:
        # for j in y:
    
    if(len(d)%2==0):
        result = (d[len(d)//2-1] + d[len(d)//2])/2
    else:
        result = d[len(d)//2-1]
    print(d)
    return result

print(median(x,y))