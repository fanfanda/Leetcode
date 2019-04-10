def mySqrt(n):
    '''二分法'''
    if n < 0: raise ValueError
    if n == 0: return 0
    if n < 1: return 1/mySqrt(1/n)
    mins, maxs, error = 0.0, n, 1e-5
    mid = (maxs + mins)/2
    temp = mid * mid
    while abs(temp - n) > error:
        if temp > n: maxs = mid
        else: mins = mid
        mid = (maxs + mins)/2
        temp = mid * mid
    return mid

def mySqrt_niudun(n):
    '''牛顿法'''
    x, error = 1, 1e-5
    temp = x * x - n
    while abs(temp) > error:
        x = x - temp/(2 * x)
        temp = x * x - n
    return x 

    

