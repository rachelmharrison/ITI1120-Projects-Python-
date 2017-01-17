#A3
#Game
#Rachel Harrison
#8617981
import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)
    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]
    shuffle_deck(deck)
    for i in range(0,len(deck)-1,2):
        other.append(deck[i])
        dealer.append(deck[i+1])
    dealer.append(deck[len(deck)-1])
    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    remove_index=[]
    l.sort()
    i=0
    l.append([None])
    while i<len(l)-1:
        if(l[i][0]!=l[i+1][0]):
            no_pairs.append(l[i])
            i+=1
        else:
           i+=2
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for i in range(len(deck)):
        print(deck[i],end=" ")
    print()
    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
    
    Precondition: n>=1
    '''
    number=(int)(input("Give me an integer between 1 and "+(str)(n)+": "))
    while(number<1 or number>n):
        number=(int)(input("Give me an integer between 1 and "+(str)(n)+": "))
    return number
            

def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]
     
    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")
    
    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)
    print("******************************************************************")

    turn=0
    while len(dealer)!=0 and len(human)!=0:
        if turn==0:
            print("Your turn.")
            print("Your current deck of cards is:")
            print_deck(human)

            print("I have",(len(dealer)),"cards.\nIf 1 stands for my first card and",(len(dealer)),"stands for my for last card, which of my cards would you like?")
            n=get_valid_input(len(dealer))
            if(n==1):
                ending="st"
            elif(n==2):
                ending="nd"
            elif(n==3):
                ending="rd"
            else:
                ending="th"
            print("You asked for my "+(str)(n)+ending,"card.")
            print("Here it is. It is",dealer[n-1])
            print("With",dealer[n-1],"added, your current deck of cards is:")
            human.append(dealer[n-1])
            dealer.remove(dealer[n-1])
            print_deck(human)
            human=remove_pairs(human)
            shuffle_deck(human)
            print("After discarding pairs and shuffling, your deck is:")
            print_deck(human)
            wait_for_player()
            turn=1
            print("******************************************************************")

            
        elif(turn==1):
            print("My turn")
            n=random.randint(1,(len(human)-1))
            if(n==1):
                ending="st"
            elif(n==2):
                ending="nd"
            elif(n==3):
                ending="rd"
            else:
                ending="th"
            print("I took your "+(str)(n)+ending,"card")
            dealer.append(human[n-1])
            human.remove(human[n-1])
            dealer=remove_pairs(dealer)
            shuffle_deck(dealer)
            wait_for_player()
            turn=0
            print("******************************************************************")

        
    if(len(dealer)==0):
        print("I do not have any more cards.\nYou lost! I, Robot, win.")
    elif(len(human)==0):
        print("You do not have any more cards.\nCongratulations! You, human, win.")

# main
play_game()
