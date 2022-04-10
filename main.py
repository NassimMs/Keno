import Handler
import os


#Gets user balance
def ReadData():
    with open("data.txt","r") as f:
        balance = f.readline()
        f.close()
    return balance


#Updates user balance
def WriteData(balance):
    with open("data.txt","w") as f:
        f.write(balance)
        f.close()



balance = int(ReadData())
username = input("Enter your Name :")
try:
    while True:
        Handler.UI()
        rep = int(input(">>"))
        if(rep == 1):
            balance = Handler.KenoGame(balance)
            WriteData(str(balance))
        elif(rep == 2):
            print(username+" has :"+str(balance)+" points")
        elif(rep == 3):
            exit()
        elif(rep == 4):
            Dirham = balance / 500
            print("You have "+str(Dirham)+" DH")
        elif(rep == 5):
            print("Withdrawing ...")
            os.system("pause")

except Exception as e:
    print(str(e))





    



