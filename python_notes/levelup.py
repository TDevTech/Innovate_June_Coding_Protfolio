import random
# floating point

# print (int (5.4))
# print (int (5.5))
# print (int (5.6))
# print (int (round(5.4)))
# # string
# print (int (54)) 
# ##print (type(int("54")))

# acc_bal = 200
# deposit = int(input("how much do you want to deposit into your Account?"))

# acc_bal += deposit
# print (f"you have {acc_bal} in your account \n")

# ## Falsy Values , Emty String , Eevry thing else is truthy

# print ("what is your name ?")
# my_name = input ()

# if my_name :
#     print (f"welcom {my_name} to code nation, Innovate L3 Coding \n ")
# else:
#     print ("you did not submit your name\n")  
#     print ("what's your name? \n")
# my_name = input ()

###

# lis_name = ["Abdo","Bob","Tarig", "Sarah", "Tom","Mercy","Steve"]
# yr_name = input ("What is your name?")

# while yr_name != lis_name [6]:
#     print ("Your name isn't on this list\n")
#     print ("try again..!!! \n")
#     yr_name ()
    #yr_name = input  ("What is your name? \n")
    # yr_name == lis_name:
    # print ("Your name is on this list\n")
    # print ("please come in..!!! \n")

### 
#acc_bal = int (200)
#deposit = input("how much do you want to deposit into your Account?\n")
# acc_update = int ()
# def acc_up ():
#     acc_bal = 200
#     deposit = input("how much do you want to deposit into your Account?")
#     print_1 = int (acc_bal) + int(deposit)
#     #print (acc_update)
# try:
#     #print (f"{(int (acc_update))}\n")
#     print (f"you have in your account {acc_up} \n")
# except:
#     print ("Please use numbers only, in this entry \n")
#     print("try again")
#     acc_up ()
# acc_up ()

####
# light = True

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()

# ### This is [] used for List , it can be changed
# even_nums =[2,4,6,8,10]
# even_nums.insert (0,0)
# print (even_nums)
# ## This is () used for Tuple , it can not be changed
# odd_nums = (1,3,5,7,9)
# odd_nums.append(11) #this would not run/work on a tuple
# print (odd_nums)

###
# Lists []
fav_songs = [  
    "George Benson – Affirmation.",
    "Bob James – Since I Fell For You.",
    "Bony James – Joy Ride.", 
    "Lonnie Liston Smith – Rainbows Of Love.",
    "Incognito – Pieces Of A Dream.",
    "Sade – Your Love Is King.",
    "Chris Botti – Good Morning Heartache.",
    "Norman Brown – After The Storm.",
    "Grover Washington Jr – Take Five."]
#print (f"{(fav_songs[2])}\n")
#start:stop:step
#print (f"{(fav_songs[0:8:2])}\n")
## slice thrugh the list 1:
#print (f"{(fav_songs[1:])}\n")

## make a string Variable

# While Loop , Brack and Contnue
## Compares and runs under condition
num = random.randint (1,49)

# while num%2==0:
#     print ("welike even numbers ! Another ..!!\n")
#     num=random.randint (1,50)
#     print("Oh No an ODD numbe...!!!\n")
###    ################################################
while True:
    num= random.randint (1,49)
    print (num)
    if num%2==0:
      print ("we like Even numbers !! add Another even ..!!\n")
      continue
    else:
       print("Oh No an ODD numbe...!!!, It's Game Over....!!! \n")
    break