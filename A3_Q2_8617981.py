#A3
#Q2
#Rachel Harrison
#8617981

def two_length_run(l):
    '''
    (List)->boolean
    Returns true if l contains a run of at least length two
    Otherwise, returns false
    '''
    for i in range(1,len(l)):
        if(l[i]==l[i-1]):
            return True
    return False

s=input("Please enter a list of numbers separated by commas: ")
l=list(eval(s))
print(two_length_run(l))

