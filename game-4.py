import random

j=3
i=0



while(j>0):
    num = random.randrange(3)

    print("0=Rock")
    print("1=Paper")
    print("2=Sizzor")
    n=int(input("Enter the choice =" ))


    if(n==0):
        if(num==0):
            print("Game is draw..")
        elif(num==1):
            print("Pc win")
            j=j-1
        else:
            print("User win")   
            i=i+1  
    elif(n==1):
        if(num==0):
            print("User win")
            i=i+1
           
        elif(num==1):
            print("Draw")
        else:
            print("Pc win")
            j=j-1
    elif(n==2):
        if(num==0):
            print("PC Win")
            j=j-1
        elif(num==1):
            print("User Win")
            i=i+1
          
        else:
            print("Draw")
    else:
        print("Enter valid input")
    print("Remaining life is =",j)
    print("Your Score is = ",i)

if(j==0):
    print("Game Over !!!")



