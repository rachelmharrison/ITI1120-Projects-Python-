import random

def perform_test(op,n):
    '''
    (int,int)->int
    if op is 0 asks n addition questions to user
    if op is 1 asks n multiplication questions to user
    if inputed answer is incorrect displays correct answer
    returns number of questions answered correctly
    '''
    correct=0
    if(op==0):
        print("Please give the answers to the following additions:")
    elif(op==1):
        print("Please give the answers to the following multipications:")
    for i in range(n):
        if(op==0):
            x=random.randint(0,9)
            y=random.randint(0,9)
            z=(int)(input((str)(x)+" + "+(str)(y)+" = " ))
            if(x+y==z):
                correct+=1
            else:
                print("Incorrect - the answer is",(x+y))
        elif(op==1):
            x=random.randint(0,9)
            y=random.randint(0,9)
            z=(int)(input((str)(x)+" * "+(str)(y)+" = " ))
            if(x*y==z):
                correct+=1
            else:
                print("Incorrect - the answer is",(x*y))
    return correct

print("Welcome to addition / multiplication test\n")
print("How many questions would you like to be tested on?")
n=(int)(input("Enter a non negative integer for the answer: "))
if(n<=0):
    print("Good bye")
else:
    print("This software tests you with",n,"questions.")
    print("0) Addition")
    print("1) Multiplication")
    op=(int)(input("Please make a selection (0 or 1): "))
    result=perform_test(op,n);


    if(result/n)>=(4/5):
        print("Well done! Congratuations.")
    elif(result/n)>=(2/3):
        print("Not too bad but please study and practice some more.")
    else:
        print("Please study more and ask your teacher for help")

