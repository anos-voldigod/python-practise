# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"what is your location in {location}")
# greet_with("aditya", "ghaziabad")


# import math
# def paint_required(height, width, cover):
#     area=height*width
#     number_of_cans=math.ceil(area/cover)
# print(f"number_of-cans")
# sample_height=int(input("height of wall is:"))
# sample_width=int(input("width of wall is:"))
# coverage=5
# paint_required(height=sample_height, width=sample_width, cover=coverage)



# #  caesar cipher#######


# alphabet=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("type 'encode' to encrypt, 'decode' to decrypt\n")
# text = input("enter your word\n").lower()
# shift = int(input("enter your word\n"))
# def encrypt(simple_text, amount_shift):
#     cipher_text = ""
#     for letter in simple_text:
#       position = alphabet.index(letter)
#     new_position = position + amount_shift
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
# print("the encoded text is {cipher_text}")
# encrypt(simple_text = text, amount_shift = shift)                 
               

# ########### dictionary #################

# student_scores={
#   "aditya":99,
#   "harsh":89,
#   "bitch":79,
#   "fuck":60,
# }

# student_grades={}
# for student in student_scores:
#   print(student)
#   score=student_scores[student]
#   if score > 90:
#     student_grades[student] = "outstanding"
#   elif score > 80:
#     student_grades[student] = "very good"
#   elif score > 70:
#       student_grades[student] = "jaa na lawde"
#   elif score > 60:
#         student_grades[student] = "fail hai bsdk"
# print(student_grades)



# my_dict={
#   "name":"[1, 2, 3, 4]",
# }

# my_dict={
#   "india":{"places_visited":["delhi", "nagpur"]}
# }


# ###### travel log ############


# travel_log=[
#     {
#     "country":"India",
#     "number of visits": 3,
#     "places visited": ["delhi", "nagpur", "nasik"]
# },
# {
#     "country":"europe",
#     "number of visits": 4,
#     "places visited": ["france", "germany", "poland"]
# },
# ]

# def add_new_country(place, total, new ):
#     new_country={}
#     new_country["country"]=place
#     new_country["number of visits"]=total 
#     new_country["places visited"]=new 
#     travel_log.append(new_country)
    
# add_new_country("russia", 2, ["moscow", "saint petersberg"])
# print(travel_log)    


# ### marks log #############

# marks_log=[
#     {
#     "student":"aditya",
#     "subjects":"maths",
#     "marks":99
# },
# {
#     "student":"harsh",
#     "subject":"maths",
#     "marks":97
# }
# ]

# def add_new_marks(name, another, number):
#     new_marks={}
#     new_marks["student"]=name
#     new_marks["subject"]=another
#     new_marks["marks"]=number
#     marks_log.append(new_marks)

# add_new_marks("daksh", "maths", "96")
# print(marks_log)    


# ############# functions with output #############


# def format_name(f_name, l_name):
#  """take a first and last name and format it to return the title case version of name."""

#  formated_f_name=(f_name.title()) 
#  formated_l_name=(l_name.title())

#  return f"{formated_f_name, formated_l_name}"

# print(format_name(input("what is your name "), input("what is your age")))


# ############ calculator #############

# def add(n1, n2): 
#     return(n1+n2)

# def sub(n1, n2):
#     return(n1-n2) 

# def mul(n1, n2):
#     return(n1*n2)

# def div(n1, n2):
#     return(n1/n2)

# operations={
#     "+":add,
#     "-":sub,
#     "*":mul,
#     "/":div
# }               

# num1=int(input("first number: "))
# num2=int(input("second number: "))

# for symbol in operations:
#     print(symbol)
# operation_symbol=input("choose one operation")
# calculation_function=operations[operation_symbol]
# answer=calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2}={answer}")

# operation_symbol=input("choose another operation")
# num3=int(input("third number"))
# calculation_function=operations[operation_symbol]
# answer22=calculation_function(num3, answer)
# print(f"{num3} {operation_symbol} {num3}={answer22}")


# ################### black jack #######################

# import random

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# # Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# and returns the score. 
# Look up the sum() function to help you do this.
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

# #   Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#   Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose "


#   if user_score == computer_score:
#     return "Draw "
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack "
#   elif user_score == 0:
#     return "Win with a Blackjack "
#   elif user_score > 21:
#     return "You went over. You lose "
#   elif computer_score > 21:
#     return "Opponent went over. You win "
#   elif user_score > computer_score:
#     return "You win "
#   else:
#     return "You lose "

# def play_game():


# #   Hint 5: Deal the user and computer 2 cards each using deal_card()
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# #   Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#   while not is_game_over:
#     Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

# #   Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# # Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

#   play_game()


# ############ scope ###############
# days=31
# def months():
#   days=30
#   print(days)
# months()
# print(days)  

# enemies="skeleton"
# def increase_enemies():
#   enemies="zombies"
#   print(f" enemies inside function= {enemies}")
# increase_enemies()
# print(f" enemies outside function: {enemies}")  

# ########## guess the number ###############3 


# from random import randint


# LEVEL_TURNS = 10
# LEVEL_TURNS = 5

# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")


# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return LEVEL_TURNS
#   else:
#     return LEVEL_TURNS

# def game():

#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
 
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     guess = int(input("Make a guess: "))

  
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

################# debugging ################

# def my_function():
#     for i in range (1, 20):
#         if i == 19:
#             print("bass kar bsdk")
# my_function()            

#################### HEART KI BACKCHODI ###################

# import turtle1
# t=turtle.Turtle()
# t.color("red")
# t.begin_fill()
# t.fillcolor("red")
# t.left(140)
# t.forward(190)
# t.circle(-90, 200)
# t.setheading(60)
# t.circle(-90, 200)
# t.forward(190)
# t.end_fill()


############## password generator ###########

# import random

# max_length = 8

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("welcome to password generator")
# print("here you can make strong passwords according to your convinience")
# nr_letters = int(input("how many letters would you like to use in your password ?? \n"))
# nr_numbers = int(input("how many numbers would you like to use ?? \n"))
# nr_symbols = int(input("how many symbols would you like to use in your password ?? \n"))

# password = ""
# for char in range(1, nr_letters+1):
#     password += random.choice(letters)

# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols+1):
#     password += random.choice(symbols) 

# print(password)           


# a=input(str())

# if a<=300 :
#     final = (a * 15 / 100) + a 
#     print(a)
#     if a>300 :
#      Final  = (a * 20 / 100) + a
#      print(a) 

# a = input(int())
# def even_odd(a):
#     if (a%2 == 0):
#         print("number is even")
#     elif (a%2 != 0):
#         print("number is odd") 
#     else:
#         print (even_odd(a))

####################################### list ####################################

######## append function ########
 
# my_list = [ 'aditya', 'naina', 'prachi', 'daksh']
# my_list.append('eiman')
# print(my_list)

########### insert function ########## 

# my_list.insert(3, 'himanshu')
# print(my_list)


######## delete element from a list #######
# my_list=['aditya', 'naina', 'prachi', 'himanshu', 'daksh', 'eiman']
# del my_list[3]
# print(my_list)

# my_list=['xvideos', 'redtub', 'ok.xxx', 'hentai', 'pornhub']
# my_list.sort()
# print(my_list)
# for reverse just use my_list.sort(reverse=True)

# cars = ['audi', 'bmw', 'porshe']
# for car in cars:
#     print(f"{car.title()}, is a nice car!")
#     print(f"{car.title()}, is a fucking car")

# squares = []
# for numbers in range(1,11):
#     square = numbers**2
#     squares.append(square)
#     print(squares)

# for value in range(1, 1000000):
#     print(value)   

# cubes = []
# for numbers in range(1, 11):
#     cube = numbers**3
#     cubes.append(cube)
#     print(cubes)

# lists = ['chal', 'na', 'lawde', 'bsdk', 'mc', 'bc']
# print("my favourite gaali is: ")
# for list in lists[:3]:
#     print(list.title())

# prices = (100, 50, 35, 160)
# print("menu for restaurant")
# print("dish_1:", prices[0])
# print("dish_2:", prices[1])

# friends = ['aditya', 'aman', 'daksh', 'mutthal']
# for friend in friends:
#     if friends=='aditya':
#         print(friend.upper())
#     else:
#         print(friend.title())

################################### OOPS ############################

# class cat:
#  """ a attempt to model a cat"""
#  def __init__(self,name,age):
#   self.name=name
#   self.age=age
#   def sit(self):
#     """to check if cat is sitting or not"""
#     print(f"{self.name} is sitting")
#   def roll(self):
#     """to check if cat is rolling or not"""
#     print(f"{self.name} is rolling")  

# class cat:
#   my_cat = cat('Willie', 6)
#   print(f"My cat's name is {my_cat.name}.")
#   print(f"My cat is {my_cat.age} years old.")

# class restaurant:
#     """attempt to model a restaurant"""
#     def __init__(self, restaurant_name, cusine_type):
#         self.restaurant_name=restaurant_name
#         self.cusine_type=cusine_type
#         def describe_restaurant(self):
#             """to describe restaurant"""
#             print(f"{restaurant_name} is s nice restaurant")
#             print(f"{restaurant_name} is located at very accessible location")
#         def cusine_type(self):
#             """to describe cusine available in restaurant"""
#             print(f"{restaurant_name} has many variety in cusine")

# #making an instance
# class restaurant:
#     best_restaurant = restaurant('taj hotel', 'cusine')
#     print(f"{best_restaurant.restaurant_name} is best restaurant across India")
#     print(f"{best_restaurant.cusine_type} is our speciality")                

# class students:
#     """modeling students of class"""
#     def __init__(self, name, subject, marks):
#         self.name = name
#         self.subject = subject
#         self.marks = marks
#     def students(self):
#         """to describe students"""
#         print(f"{self.name} is a good student")
#     def subject(self):
#         """subject description"""
#         print(f"{self.subject} is a easy subject for {self.name}.")
#     def marks(self):
#         """marks of student"""
#         print(f"{self.name} has scored {self.marks}.")
# class student:
#     class_student = students('Aditya', 'Maths', 99)
#     another_student = students('Utkarsh', 'maths', 98)
#     print(f"student name is {class_student.name}.")
#     print(f"{class_student.subject} is very scoring subject.")
#     print(f"marks obtained are {class_student.marks} in the following subject.")

#     print(f"\nanother student name is {another_student.name}")
#     print(f"another student also scored marks in {another_student.subject}")
#     print(f"marks obtained by this student is {another_student.marks}")
#     print(f"bahot chewtiya baacha hai {another_student.name}")

# amount = 0
# x =int(input("enter a number"))
# if x<=100:
#     print("amount")
#     if x>100 & x<=200:
#         amount = amount*5
#     if x>200:
#         amount = 500 + (amount-200)*100
# print("amount to pay", amount)
        
# a = int(input("enter a number"))
# b = int(input("enter another number"))
# c=a
# a=b
# b=c
# print("value of a after swapping:", a)
# print("value of b after swapping:" , b)

# class cars:
#     """modeling cars"""
#     def __init__(self, name, color):
#         self.name = "audi"
#         self.color = "black"
#         self.odometer = 0
#     def car_description(self):
#         """description about cars"""
#         print(f"{self.name} is a badass car. ")
#     def car_color(self):
#         """description of color of car"""
#         print(f"{self.name} looks very awesome in {self.color}")
#     def odometer(self) :
#         """to show position of odometer of car""" 
#         print(f"odometer reading")

# class car:
#     class_car = cars('audi', 'black')
#     print(f"{class_car.name} is a badass car to drive")
#     print(f"{class_car.name} looks very cool ")
#     print(class_car.car_description())
#     class_car.odometer()

# item1 = 'phone'
# item1_price = 100000 
# item1_quantity = 1 
# item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

################# shapes(turtle) ############

             # square
# import turtle
# aditya = turtle.getscreen()
# aditya.bgcolor("blue")
# turtle.speed(1)
# t1 = turtle.Turtle()
# t1.forward(100)
# t1.left(90)
# t1.forward(100)
# t1.left(90)
# t1.forward(100)
# t1.left(90)
# t1.forward(100)
            # OR
# from turtle import*
# pensize(3)
# i=0
# while i<4:
#     for i in range(4):
#         forward(160)
#         left(90)
#     i+=1
            # circle
# import turtle
# aditya = turtle.getscreen()
# t1 = turtle.Turtle()
# turtle.speed(1)
# t1.circle(100)

            # hexagon 
# from turtle import*
# pensize(4)
# for i in range(6):
#     forward(100)
#     left(60)

            # triangle
# import turtle
# aditya = turtle.getscreen()

# t1 = turtle.Turtle()
# t1.forward(100)
# t1.left(120)
# t1.forward(100)
# t1.left(120)
# t1.forward(100)
# turtle.done()

       # OR
# from turtle import*
# for i in range(3):
#     forward(300)
#     left(120)

       # OVAL
# from turtle import*
# shape("circle")     
# shapesize(10, 5, 2)  
# turtle.done()

# from turtle import*
# speed(1)
# bgcolor("black")
# color("greenyellow")
# pensize(5)
# for i in range(8):
#     forward(100)
#     left(45)

         ## STAR 
# from turtle import*
# color('red', 'yellow') 
# begin_fill() 
# while True:
#        forward(200) 
#        left(170) 
#        if abs(pos())<1:
#               break
# end_fill()
# done() 

         ## DOT CIRCLE
# import turtle
# t = turtle.Turtle()
# t.dot(100)
# turtle.mainloop()

# import turtle
# t1 = turtle.Turtle()
# t1.pensize(4)
# t2 = t1.clone()
# t2.pensize(4)
# t1.color("black")
# t2.color("pink")
# t1.circle(30)
# t2.circle(40)
# for i in range(50, 100, 20):
#        t2.circle(i)
#        turtle.mainloop()     

        # SPIRAL CIRCLES
# import turtle
# t = turtle.Turtle()
# turtle.bgcolor("black")
# turtle.speed(0)
# t.pensize(2)
# while True:
#        for i in range(6):
#               for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
#                      turtle.color(colors)
#                      turtle.circle(100)
#                      turtle.left(10)
# turtle.hideturtle()  
# turtle.mainloop()   

# import turtle
# t = turtle.Turtle()
# aditya = turtle.getscreen()
# aditya.bgcolor("black")
# turtle.pensize(2) 
# # to design the curve 
# def curve():
#        for i in range(200):
#               t.right(1)
#               t.forward(1)
#               t.speed(2)
#               t.color("red", "pink")
# t.begin_fill()
# t.left(140)            
# t.forward(111)
# curve()
# t.left(120)
# curve()
# t.forward(111)
# t.end_fill()
# t.hideturtle()
# turtle.mainloop()

# class country:
#        """to model a description of a country""" 
#        def __init__(self, name, people):
#               self.name=name
#               self.people=people
#        def place(self):
#               """to name the country"""
#               print(f"{self.name} is a good country")
#        def description(self):
#               """description of people"""
#               print(f"{self.people} are very good in nature")

# class country:
#        my_country = country('India', 'indians')
#        print(f"{my_country.name} is a very good and prosporous country.")
#        print(f"{my_country.people} are very generous people among others.  ")                            

# def area(length, width):
#        area = length* width
#        return area
# length = float(input("enter length"))
# width = float(input("enter width"))
# print("area of rectangle is: ", area(length, width))

# def aditya(name, gender, quality = 'intelligent'):
#        """display information"""
#        print(f"My name is {name}")
#        print(f"{name} is {gender}")
#        print(f"{name} is a very {quality} boy.")
      
# aditya('Aditya','male')
# aditya('harsh', 'male')

# def shirts(company, size, message='GIVE UP YOUR DREAMS AND DIE'):
#        """display information of shirts"""
#        print(f"Shirts of {company} are very popular these days")
#        print(f"Mostle size of {size} are available for the customers")
#        print(f"{message}")
# shirts('Zara', 'XL')     

# s1 = "Aditya"
# print("initial string")
# print(s1[0])   # to access a character in a string
# print(s1[-1])
# print(s1[::-1])  #reversing a string

# s1 = "adityatyagi"
# print("initial string")
# print(s1[2:7])   # slicing a string

# s1 = "my name is aditya"
# print("initial string: ")
# print(s1)
# s1 = "my name is aditya tyagi"
# print("new string")
# print(s1)        # updating new element to a string ( we have to replace a new string as  strings are immutable)

# del keyword is used to delete a string


###################### polymorphism #######################
# polymorphism means the same function name (but different signatures) being used for different type

# class aditya:
#        def name(self):
#               print("My name is Aditya")
#        def about(self):
#               print("Aditya is a brillant student") 
#        def type(self):
#               print("Aditya scores very good marks")

# class Harsh:
#        def name(self):
#               print("Student nname is Harsh")
#        def about(self):
#               print("Harsh is an average student")
#        def type(self):
#               print("Harsh scores average marks")   
# obj_aditya = aditya()
# obj_harsh = Harsh()
# for students in (obj_aditya, obj_harsh):
#        students.name()
#        students.about()
#        students.type()

####################### tkinter #######################

# from tkinter import*
# aditya_root = Tk()

# #width x height
# aditya_root.geometry("400x400")
# #minsize = for defining minimum size of console screen  maxsize = for defining maximum size of console screen 
# aditya_root.minsize(300,200)
# aditya = Label(text="This is my first GUI")
# aditya.pack()
# aditya_root.mainloop()

# from tkinter import*
# aditya_root = Tk()
# aditya_root.geometry("500x400")
# photo = PhotoImage(file="1.pnj")
# aditya = Label(image=photo)
# aditya.pack()
# aditya_root.mainloop()

# from tkinter import*
# root = Tk()
# root.geometry("500x400")
# root.title("My gui")
# important label options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# title_label = Label(text =''' Recently i read a book name something i never told, 
#                     which is an amazing book to read for 
#                     people who are one sided lovers'''
#                     , bg = "yellow", fg = "red", padx = 65, pady = 45, font = ("comicsansms", 10), borderwidth=3, relief=SUNKEN)

# important pack options
# side = top, bottom, right, left
# ancor
# title_label.pack(side = TOP, fill=Y, padx=35, pady=35)         # nw = northwest ne = northeast 
# root.mainloop()

# from tkinter import*
# root = Tk()
# root.geometry("650x330")
# def hello():
#        print("hello guys")
# F1 = Frame(root, bg="grey", borderwidth=5)
# F1.pack(side=TOP, fill="x")

# F2 = Frame(root, bg = "grey", borderwidth=5)
# F2.pack(side=LEFT, fill="y")

# l2=Label(F2, text="menu")
# l2.pack(pady=32)

# l=Label(F1, text="Aditya", font="Helvetica 16 bold", fg="red")
# l.pack(pady=22)

# b1 = Button(F1, fg="red", text="click here", command=hello)
# b1.pack()

# b2 = Button(F2, fg="red", text="Files")
# b2.pack(side=BOTTOM)

# root.mainloop()

# from tkinter import*
# def getvals():
#        pass
# root = Tk()
# root.geometry("650x350")
# def hello():
#        print("Submission Done")
       
# user = Label(root, text="username")
# password = Label(root, text="password")
# user.grid()
# password.grid(row=1)      # .grid is used to make rows and columns

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

# uservalue = StringVar()
# passvalue = StringVar()

# user_entry = Entry(root, textvariable = uservalue)
# pass_entry = Entry(root, textvariable = passvalue)

# user_entry.grid(row=0, column=1)
# pass_entry.grid(row=1, column=1)

# btn = Button(text="submit", command = hello)
# btn.grid()

# root.mainloop()

###############################################################################

# class cat:
#  """ a attempt to model a cat"""
#  def __init__(self,name,age):
#   self.name=name
#   self.age=age
#   def sit(self):
#     """to check if cat is sitting or not"""
#     print(f"{self.name} is sitting")
#   def roll(self):
#     """to check if cat is rolling or not"""
#     print(f"{self.name} is rolling")  

# class cat:
#   my_cat = cat('Willie', 6)
#   print(f"My cat's name is {my_cat.name}.")
#   print(f"My cat is {my_cat.age} years old.")


# class person:
#        """details about favourite person"""
#        def __init__(self, name):
#               self.name=name
#               def about(self):
#                      """who is my favourite person"""
#                      print(f"{self.name} is my favourite person")
                     
# class person:
#        my_person = person('naina')
#        print(f"{my_person.name} is my favourite person")

                  ############ revision ############# 
# friend = ['aditya', 'aman', 'daksh', 'naina']
# for friends in friend:
#        if friends == 'aditya':
#               print(friends.upper())
#        else:
#               print(friends.title())
              
# age = int(input("enter your age"))
# if age>=18:
#        print("you can vote")
# else:
#        print("you are underaged")          

############### lambda function : it is a function that can take any number of arguments but can only have one expression ################## 

# x = lambda a : a+10
# print(x(5))                  

# x = lambda a : a*10
# print(x(5))

# x = lambda a,b,c : a*b*c
# print(x(2,3,4))

# def myfunction(n):
#        return lambda a : a*n
# doubles = myfunction(2)
# print(doubles(11))

# def myfunction(n):
#        return lambda a : a*n
# def Myfunction(m):
#        return lambda b : b*m
# doubles = myfunction(2)
# print(doubles(222))
# triples = Myfunction(3)
# print(triples(333))

# from tkinter import*
# aditya_root = Tk()
# aditya_root.geometry("400x400")
# aditya_root.minsize(300,200)
# aditya = Label(text = " Ugly love by Collean Hoover. ")
# aditya.pack()
# aditya_root.mainloop()

# from tkinter import*
# aditya_root = Tk()
# aditya_root.geometry("600x400")
# def acha_bhai():
#        print("chal na chewtiye")
# F1 = Frame(aditya_root, bg = "black", borderwidth=60)
# F1.pack(side=TOP, fill="x")   

# l1 = Label(F1, text="UGLY LOVE")
# l1.pack(padx=30)

# F2 = Frame(aditya_root, bg = "black", borderwidth=30)
# F2.pack(side=LEFT, fill="y")

# l2 = Label(F2, text="content")
# l2.pack(pady=30)

# b1 = Button(F2, fg="grey", text="click here")
# b1.pack()

# aditya_root.mainloop()




# from tkinter import*
# aditya_root = Tk()
# aditya_root.geometry("600x400")

# var1 = IntVar()
# Checkbutton(aditya_root, text="want to read ?? ", variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(aditya_root, text="don't want to read.")
# mainloop()

from tkinter import*
