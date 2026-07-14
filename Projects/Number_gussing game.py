import random
print("Play the GOVI's Number gussing name")

actual_num = random.randint(1,100)
try:
    for i in range(0,11):
        user_num = int(input("Enter the number between 1 to 100:"))
        if user_num < 1 or user_num > 100 :
           print("Check your input is in  the range of 1 to 100")
        elif user_num > actual_num:
           print("My number is lesser than", user_num)
        elif user_num < actual_num:
            print(" My number is Greater than", user_num)
        else:
            print(" CORRECT! You Win")    
            break
    if user_num == actual_num:
        print(" You gussed the number in", i ,"attempts")
    else :
        print("Oops,You are out of the chance try again")   
except ValueError:
       print(" Character are not allowed enter the Number ")    