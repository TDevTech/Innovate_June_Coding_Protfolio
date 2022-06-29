
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
acc_update = int ()
def acc_up ():
    acc_bal = 200
    deposit = input("how much do you want to deposit into your Account?")
    print (int (acc_bal) + int(deposit))
    #print (acc_update)
try:
    #print (f"{(int (acc_update))}\n")
    print (f"you have in your account {acc_up} \n")
except:
    print ("Please use numbers only, in this entry \n")
    print("try again")
    acc_up ()
acc_up ()