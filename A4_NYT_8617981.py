#A4 Part 2
#Rachel Harrison
#8617981

def bookFormat(book):
    '''
    (2D list)-> String
    returns each index of book formatted as a string
    '''
    return ('"'+book[0]+'" by '+book[1]+' ('+book[3]+')')

def yearRange(books):
    '''
    (2D list)-> None
    Prints the books who reached bestseller status between the two years inputed by the user
    '''
    print("")
    year1=(input("Please enter the first year: "))
    valid=False
    while valid==False:
        if (year1.isdigit()==True and (int)(year1)>999 and (int)(year1)<10000):
            valid=True
        else:
            year1=input("Year must be a four digit integer: ")

    year2=(input("Please enter the second year: "))
    valid=False
    while valid==False:
        if (year2.isdigit()==True and (int)(year2)>999 and (int)(year2)<10000):
            valid=True
        else:
            year2=input("Year must be a four digit integer: ")
    print("")
    print("The bestsellers between",year1,"and",year2,"are:")
    found=False
    
    for year in range((int)(year1),(int)(year2)+1):
        for i in range(len(books)):
            if((str)(year) in books[i][3]):
                print(bookFormat(books[i]))
                found=True
    if(found==False):
        print("No books found")
    print("")

def monthYear(books):
    '''
    (2D list)-> None
    Prints the books who reached bestseller status in the year and month inputed by user
    '''
    print("")
    year=(input("Please enter the year: "))
    valid=False
    while valid==False:
        if (year.isdigit()==True and (int)(year)>999 and (int)(year)<10000):
            valid=True
        else:
            year=input("Year must be a four digit integer: ")

    month=(input("Please enter a month (1-12): "))
    valid=False
    while valid==False:
        if (month.isdigit()==True and (int)(month)>0 and (int)(month)<13):
            valid=True
        else:
            month=input("Month must be an integer from 1-12: ")
    found=False
    print("")
    print("The bestsellers from",month+"/"+year,"are:")
    for i in range(len(books)):
        if (year in books[i][3]):
            if ((int)(month)<10 and books[i][3][0]==month[0]):
                print(bookFormat(books[i]))
                found=True
            elif(books[i][3][0]==month[0] and books[i][3][1]==month[1]):
                print(bookFormat(books[i]))
                found=True

    if(found==False):
        print("No books found")
    print("")
        

def author(books):
    '''
    (2D list)-> None
    Prints the books whose author's names contain string author
    '''
    print("")
    author=input("Please enter author's name (or part of a name): ")
    author=author.lower()
    print("")
    print("The bestsellers written by an author whose name contains",author,"are:")
    found=False
    for i in range(len(books)):
        if author in books[i][1].lower():
            print(bookFormat(books[i]))
            found=True
    if found==False:
        print("No books found")
    print("")

def title(books):
    '''
    (2D list)-> None
    Prints the books whose titles contain string title
    '''
    print("")
    title=input("Please enter title (or part of title): ")
    title=title.lower()
    print("")
    print("The bestsellers whose title contains",title,"are:")
    found=False
    for i in range(len(books)):
        if title in books[i][0].lower():
            print(bookFormat(books[i]))
            found=True
    if found==False:
        print("No books found")
    print("")
    
def xBestsellers(f):
    '''
    (2D List) -> None
    prints the authors with at least x bestsellers
    '''
    print("")
    x=(input("Please enter an integer greater than zero: "))
    valid=False
    while valid==False:
        if (x.isdigit()==True and (int)(x)>0 and ("." not in x)):
            valid=True
        else:
            x=input("Must be an integer greater than zero: ")
    f.sort()
    print("")
    print("The authors with at least",x,"bestsellers are:")
    found=False
    i=len(f)-1
    x=(int)(x)
    while f[i][0]>=x:
          print(f[i][1]+" with",f[i][0],"bestsellers.")
          found=True
          i-=1
          
    if found==False:
        print("No authors found")
    print("")

def mostBestsellers(f):
    '''
    (2D list)->None
    prints the top x authors in terms of number of bestsellers
    '''
    print("")
    x=(input("Please enter an integer greater than zero: "))
    valid=False
    while valid==False:
        if (x.isdigit()==True and (int)(x)>0 and ("." not in x)):
            valid=True
        else:
            x=input("Must be an integer greater than zero: ")
    f.sort()
    x=(int)(x)
    print("")
    print("The top",x,"authors with the most bestsellers are:")
    found=False
    for i in range(len(f)-1,len(f)-(x+1),-1):
        print(f[i][1]+" with",f[i][0],"bestsellers.")
    print("")


def frequency(books):
    '''
    (2D List)-> 2D List
    returns f, the number of times each author appears in books
    first value in f is number of appearances, second is author's name
    '''
     f=[]
     for i in range(len(books)):
          same=False
          for j in range(len(f)):
               if(books[i][1]==f[j][1]):
                    f[j][0]=f[j][0]+1
                    same=True
          if(not(same)):
               f.append([1,books[i][1]])
     return f

#Main
lines=open("NYT-bestsellers.txt").read().splitlines()
books=[]
for line in lines:
    books.append(line.split('\t'))

for i in range(len(books)):
    for j in range(len(books[i])):
        books[i][j]=books[i][j].strip()
entry=""
while (entry!="q" and entry!="Q"):
    valid=False
    while valid==False:
        print("====================================================================")
        print("Menu:")
        print("1) Look up bestsellers by year range")
        print("2) Look up bestsellers by month and year")
        print("3) Look up bestsellers by author")
        print("4) Look up bestsellers by title")
        print("5) Look up authors with a certain number of bestsellers")
        print("6) Look up a certain number of authors with the most bestsellers")
        print("Q) Quit")
        entry=input("Answer (1,2,3,4,5,6,Q): ")
        print("====================================================================")
        selection=0
        if(entry.isdigit()==True):
            selection=(int)(entry)
            if(selection>0 and selection<7):
                valid=True
        if(entry=="q" or entry=="Q"):
            valid=True       
    if(selection==1):
        yearRange(books)
    elif(selection==2):
        monthYear(books)
    elif(selection==3):
        author(books)
    elif(selection==4):
        title(books)
    elif(selection==5):
        xBestsellers(frequency(books))
    elif(selection==6):
        mostBestsellers(frequency(books))



