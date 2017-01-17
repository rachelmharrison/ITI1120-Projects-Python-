#A3
#Q1
#Rachel Harrison
#8617981

def count_pos(l):
    '''
    (List)->int
    Returns number of positive numbers (ie greater that 0) in l
    Preconditions: all elements of l must be numbers
    '''
    counter=0
    for i in range(len(l)):
        if(l[i]>0):
            counter+=1
    return counter

s=input("Please enter a list of numbers separated by commas: ")
l=list(eval(s))

print("There are",count_pos(l),"positive numbers in your list")

    
