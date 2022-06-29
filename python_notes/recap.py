import random
import numbers

# print ("This is Python Recap Notes")

# greeting = "Wellcom to L3 Innovate Coding ..!!!"

# print (greeting)

# print ("This a string for displaying characters 123, @~&, !!!")

# print ("This Numbers: 0, 1, 2, 3, ... 1000 !!!")

# print (0, 1, 2, 3, + 1000)

# print (1.63* 10)

# print (True)

# print (False)

# print (None)

# # motheds

# print(len(greeting))

# print(len(greeting[1]))

# print(greeting.upper())

# print("HELLO".lower())

# print("hello everyOne. THIS IS Innovate".capitalize())

# print("This quick brown fox Fox fox fox".count("fox "))

# print("This quick brown fox".find("b"))

# print ("The quick brown fox".replace("fox","frog"))

# print ("this quick brown fox             ".strip())

# print ("this quick brown fox             ".strip("fox"))

# # Libary

# print(random.random())

# print(random.uniform(1, 10))

# print(random.randint(1,10))

# # Veriables=> snake_case

# my_name = "Tarig"
# my_age = 45
# student = True
# # print the values of those veriables
# print(my_name,my_age,student)
# # print text + veriable
# print("Hello my name is "+ my_name)

# #print("I am + my_age")

# #print("Student"+ student)
# # uses {} as placess holder, 
# print("Hello my name is {} and I am {} years old".format(my_name,my_age))
# # f string, new best practise
# print(f"Hello my name is {my_name} and I am {my_age} years old")

# ##
# # Addition
# print (10+65)
# #Subtraction
# print (100-25)
# # Multiple
# print (3*9)

# print (66**99)
# # Division
# print (18/9)

# print (75/3)

# print (75/2)
# # Modulus >> Division with Reminder
# print (75%3)

# print (75%2)
# #
# balance = 100
# print (balance)
# amount = 20

# #balance = amount + balance
# balance += amount
# print (balance)

# # inputs

# answer = input ("What is your name?")

# print (answer)

# # \n scape Character for new line

# answer = input ("What is your name? \n")

# print (answer)

# # if alse statment

# music = "smooth Jazz"

# if music == "smooth Jazz":
#     print ("Nice, Cool, It's Great Smooth Jazz Music")
#     print ("turn it on")
#     print ("Keep it on")
# elif music == "classical":
#     print ("Oh no, no, it's classical")
#     print ("turn it off")
# else:
#     print ("No Music is Playing")

# # Comparison Operaters == Equal and != Not Equal

# # Modules % == > < => <=

# print (10%2==0)

# print (10%3==0)

# num1  = 100
# num2 = 500

# if num1 > num2:
#     print(f"{num1} is bigger")
# elif num2 > num1:
#     print (f"{num2} is bigger")
# else:
#     print ("Both are equal, {num1} = {num2}")

# # And  operater
# day_tem = "High"
# weather = "Sunny"

# if day_tem == "High" and weather == "Sunny":
#     print ("To day is a very hot, Drink alot of water, Stay in the shade... \n") 
# elif day_tem == "Low" and weather == "Snowing":
#     print ("To day is cold, Wear Coat and Drink hot Coffe or Tea...\n") 
# else:
#     print ("To day is Fine Day, enjoy it out side... \n") 

# # OR operater
# bulb = "burned"
# switch = "off"
# power = "off" 

# if bulb == "burnd" or switch == "off" or power == "off":
#     print ("Please check Bulb is replaced and The power is on..\n ")
# else:
#     print ("The Bubl Light is Turn ON")
# # Functions
# # print , input
# #  def 

# def light_switch():
#     print ("Switching The Lights")
#     light_switch()
#     light_switch()
#     light_switch()


# amount = 700
# accnum = 100900

# def bank_balance (amount, accnum):
#     print (f"You have withdrawn {amount} from your bank account {accnum}. \n")
#     bank_balance (150, 100700)

# Lists []
# fav_songs = [  
#     "George Benson – Affirmation.",
#     "Bob James – Since I Fell For You.",
#     "Bony James – Joy Ride.", 
#     "Lonnie Liston Smith – Rainbows Of Love.",
#     "Incognito – Pieces Of A Dream.",
#     "Sade – Your Love Is King.",
#     "Chris Botti – Good Morning Heartache.",
#     "Norman Brown – After The Storm.",
#     "Grover Washington Jr – Take Five."]
# print (f"{fav_songs}\n")

# print (f"{fav_songs[3]}\n")

# fav_songs[7] = "Norman Brown – After The Storm."
# print (f"{fav_songs}\n")

# print (len(fav_songs))

# fav_songs.append ("Bony James – Joy Ride.")
# print (f"{fav_songs}\n")

# fav_songs.pop ()
# print (f"{fav_songs}\n")

# fav_songs.sort ()
# print (f"{fav_songs}\n")

# fav_songs.reverse ()
# print (f"{fav_songs}\n")

# fav_songs.count (7)
# print (f"{fav_songs}\n")

# fav_songs.remove ("Lonnie Liston Smith – Rainbows Of Love.")
# print (f"{fav_songs}\n")

# # fav_songs.extend ()
# # print (f"{fav_songs}\n")

# For Loops

# for i in fav_songs:
#    print ("That's a great song")

# for i in range(9):
#     print (i)

# for i in range (0, 9):
#     print (i)

# # (Start:Stop:Step)
# for i in range(2,9,2):
#     print (i)

# for i in range(9,-1,-1):
#     print (i)


# # While Loops

# num = 0 

# while num != 0:
#     print (num)
# # Ctrl + C to stop / kill the while loops

# while num < 10:
#     num += 1
# print (num)
# # Ctrl + C to stop / kill the while loops

# import random and While Loops
#import random

myfav_num = 15

rand_num = random.randint (0,49)

while myfav_num != rand_num:
    #print (f"Your number {rand_num}, do not match the computer {rand_num}...!! \n" )
    print(f"Your number {myfav_num} and {rand_num} do not match\n")
    
    rand_num = random.randint(0,49)
    #rand_num ==  myfav_num
    #print(f"Your number {myfav_num} and {rand_num} do match\n")
    print (f"Your {myfav_num} has been found and do match the computer {rand_num}...!! \n")



