#Assignment 5
#Part 1
#Rachel Harrison
#8617981

def largest_34(a):
    '''(List)->Number,Number'''
    a.sort()
    return a[-3]+a[-4]

def largest_third(a):
    '''(List)->Number'''
    a.sort()
    total=0
    for i in range(len(a)-1,len(a)-len(a)//3-1,-1):
       total+=a[i]
    return total

def third_at_least(a):
    '''(List)->Number'''
    a.sort()
    counter=1
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            counter+=1
            if counter==(len(a)//3+1):
                return a[i]
        else:
            counter=1
    return None

def sum_tri(a,x):
    '''(List,Number)->boolean'''
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i]+a[j]+a[k]==x:
                    return True
    return False
