#Assignment 5
#Part 3
#Rachel Harrison
#8617981

def digit_sum(n):
    '''(int)->int'''
    if(n<10):
        return n
    else:
        return n%10 + digit_sum(n//10)

def digital_root(n):
    '''(int)->int'''
    if(n<100):
        return digit_sum(n)
    else:
        return digital_root(digit_sum(n))
        
