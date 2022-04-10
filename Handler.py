import os
import time
import Keno




def UI():
    print("------------------------------")
    print("------------------------------")
    print("~~~~~~~~~~Welcome to Keno Games~~~~~~~~~~~~~")
    print("------------------------------")
    print("------------------------------")

    print("1/ Play Keno Match ")
    print("2/ Check Balance")
    print("3/ Quit")
    print("4/ Convert to DH")
    print("5/ Withdraw")
    


def Winings(win):
    print("You won "+str(win)+" points")

def Losings(lose):
    print("You Lost "+str(lose)+" points")




def KenoGame(balance):
    if(balance > 0):
        user_guess = []
        keno_numbers = []
        score = 0
        num_count = int(input("How many numbers you want to play ? :"))
        playcash = int(input("How many points you want to play with ? :"))
        # Gestion User Input
        if(num_count > 5 or playcash > balance):
            print("Error")
            pass
        else:
            # User Numbers
            for num in range(num_count):
                num = int(input("Enter your "+str(num+1)+" number :"))
                user_guess.append(num)

            # Start Keno 
            keno_numbers = Keno.CreateNumbers()
            Keno.ShowNumbers(keno_numbers)
            score = Keno.CheckNumbers(user_guess,keno_numbers)


            # Gestion dial Balance
            if(num_count == 1):
                if(score == 1):
                    balance = balance + playcash * 2
                    Winings(playcash*2)
                else:
                    balance = balance - playcash
                    Losings(playcash)
            elif(num_count == 2):
                if(score == 2):
                    Winings(playcash*10)
                    balance = balance + playcash * 10
                else:
                    balance = balance - playcash
                    Losings(playcash)
            elif(num_count == 3):
                if(score == 3):
                    Winings(playcash*25)
                    balance = balance + playcash * 25
                elif(score == 2):
                    Winings(playcash*2)
                    balance = balance + playcash * 2
                else:
                    balance = balance - playcash
                    Losings(playcash)
            elif(num_count == 4):
                if(score == 4):
                    balance = balance + playcash * 50
                    Winings(playcash*50)
                elif(score == 3):
                    balance = balance + playcash * 5
                    Winings(playcash*5)
                elif(score == 2):
                    balance = balance + playcash * 1
                    Winings(playcash*1)
                else:
                    balance = balance - playcash
                    Losings(playcash)
            elif(num_count == 5):
                if(score == 5):
                    balance = balance + playcash * 500
                    Winings(playcash*500)
                elif(score == 4):
                    balance = balance + playcash * 15
                    Winings(playcash*15)
                elif(score == 3):
                    balance = balance + playcash * 2
                    Winings(playcash*2)
                else:
                    balance = balance - playcash
                    Losings(playcash)

            print("-------------------------------")
            print("Your Score is :"+str(score))
            time.sleep(7)
            os.system("cls")
            return balance
    else:
        print("You don't have points in your Account")
