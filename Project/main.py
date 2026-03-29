computer=-1
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
if(computer==you):
    print("It's a tie")
else:
    if(computer ==-1 and you==1):
        print("You win")
    elif(computer == -1 and youstr == 1):
        print("You win")
    elif(computer == 0 and youstr == -1):
        print("You win")
    elif(computer == 1 and youstr == 0):
        print("You win")
    elif(computer == youstr):
        print("It's a tie")
    else:
        print("You lose")