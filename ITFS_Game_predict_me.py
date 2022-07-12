from num2words import*
from random import *
print("\tWELCOME TO GAME PREDICT ME\n")
print("Instructions: \n\tYou have maximum 12 guess\n\tNumber must be in 1 to 1000\n")
#creating a random number between 1 & 1000
def random_num():
    r=randint(1,1000)
    #print(r)
    return r

def guess(a):
    
    count=0
    print("Lets start!")
    for i in range(12):
        count=count+1
        n=int(input("enter a number between 1 and 1000:")) #taking input from user
        while n not in range(1,1001):
            n=int(input("Please enter a number between 1 and 1000:"))
        if n==a:
            print("!!!Congratzzz!!!!...You guesss correctly\n\t","its '",num2words(n),"'")
            break
        elif n>a+30:
            print("your guess is too big")
        elif n<a-30:
            print("Your guess is too small")
        elif n>a:
            print("your guess is still big")
        else:
            print("your guess is still small")
        if count==5: 
            if a%2==0:
                print("\n********** Hint 1: The number is a even number **********")
            else:
                print("\n********** Hint 1: The number is odd number *******")
        if count==10:
            s=a-5
            s1=a+5
            print("\n*******Hint 2: The number is in range %d and %d *******"%(s,s1))
        if count==12:

            print("No more chance, You reached maximum guess limit")
    
    if n==a or count==12:
        print("Do you wanted  to play again? Yes | No")
        ch=0
        while ch not in ['yes'.upper(),'no'.upper()]:
            
    
            ch=input().upper()
            if ch=='YES':
                m=random_num()    
                guess(m) 
            elif ch=="NO":
                print("Ok, Goob bye. see u soon!")
            else:
                print("Please Type Yes or No")
            
            
        
a=random_num()
guess(a)


