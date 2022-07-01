
# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")

#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use numbers only")
#         print("try again")
#         add_up()
# add_up()

import random
#user_num = input ("Enter your numer here...\n")
def game_run ():
    user_num = input ("Enter your numer here...\n")
    num1 = user_num
    print (num1)
    try:
        print(int (num1))
        print(type(int(num1)))
    except:
        print("Please use numbers only\n")
        print("try again..\n")
        game_run()
game_run ()









