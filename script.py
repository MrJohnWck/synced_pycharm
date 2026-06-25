#pick=23
#print(type(pick))
#from idlelib.pyshell import capture_warnings
#from os import WCONTINUED
import random
from asyncio import print_call_graph
from enum import nonmember

#human = False
#print(type(human))
#print("are you a human? "+str(human))

#first=4
#second="ok"
#full=first+" "+second
#print(full)


#x=22
#y=22.5
#print(x+y)
#print(x-y)
#print(x*y)


#x="9.23"
#x=float(x)
#print(x)


#name=input("What is your name?")
#age=input("How old are you? ")
#y=input("why are you so dumb? ")
#print("so you're " +age+ " years old,"+" your name is "+str(name)+" and you're dumb "+str(y))


#name="AaBbCcAa"
#print(name.capitalize())
#print(name.title())
#print(name.lower())
#print(name.upper())
#print(len(name))
#print(name.isdecimal())
#print(name.replace("a", "A", 2))


#age=input("What is your age? ")
#if int(age)<=14: print("you're too young.")
#if 14<=int(age)<=24: print("you are underage")
#if 50>=int(age)>=24: print("you are "+str(age)+" years old.")
#else: print("You are "+str(age)+" years old, which isnt nice.")


#age=input("what is your age?")
#if 0<=int(age)<=18: print("You are a child, and you are", int(age), "years old.")
#elif 18<=int(age)<=30: print("You are a millenial.")
#elif 30<=int(age)<=50: print("You are getting old.")
#elif 50<=int(age)<=75: print("You are old.")
#else:
 #   age_old=input("How are you even alive?")
  #  print(age_old)



#while 1==1:
   # print("what is happening")

#name = " "
#while len(name)==1:
  #  name=input("Enter your name: ")
   # print("hello "+name)


#while 1==1:
    #print("this is a 1 minute timer")
    #for index in range(1,61):
    # print(index)

#while 1==1:
  #  print("idk")
   # for timer in range(2,121,2):
    #    print(timer)

    #for ok in "WHAt is happening.":
    #print(ok)



#import time

#for seconds in range(10, 0, -1):
 #print(seconds)
 #time.sleep(1)
#print("hehe")


#print("This is a (infinite) 1 minute timer.")
#import time
#while 1==1:
 ##  print(seconds)
   # time.sleep(1)
 #print("1 minute has passed")



#rows=int(input("How many rows would you like?"))
#columns=int(input("How many columns would you like?"))
#symbol=input("What symbol would you like?")

#for index in range(rows):
 # for oopy in range(columns):
  #    print(symbol, end="")
  #print()



#while 1==1:
 #   name=input("What name would you like?")
 #   if len(name)!= 0:
  #      break
   # else: print("Please enter a valid name")
    #continue
#print("thank you "+name)



#phone ="123-434-5335-535"
#for index in phone:
 #   if index=="-":
  #      continue
   # print(index, end="+")



#while 1==1:
 #for i in range(1,21):
   # if i==17:
   #     pass
  #  elif i==13:
  #      continue
  #  elif i==19:
  #      break
  #  else: print(i, 3, end=" ")




#games=["codm", "rl", "gta SA", "FN"]
#print(games)
#print(games[3])
#print(games[1])
#games[2]="fall"
#print(games)

#games.append("hehe")
#for x in games:
 #   print(x)

#games.remove("codm")
#games.pop()
#games.sort()
#for x in games:
 #   print(x)



#drinks=["coffee", "tea", "soda"]
#dinner=["roti", "sabsi"]
#dessert=["chocolate","ice cream", "waffle"]

#edible=[drinks, dinner, dessert]

#print(edible[1])
#print(edible[2])
#print(edible[1][0])



#student=("bruh",21,"male")
#print(student.count("male"))
#print(student.count("female"))
#print(student.index(21))
#print(student.index("bruh"))

#for x in student: print (x)
#if "bro" in student:
 #   print("hehe")
#else: print("no")




#set is basically a list, but it doesnt allow duplicate values, and it does not print them in order.
#utensils={"katori", "fork","spoon", "knife"}
#utensils.add("plate")
#utensils.remove("katori")
#utensils.clear()
#for x in utensils: print (x)

#food={"roti", "sabsi", "chawal", "fork"}
#utensils.update(food)
#food.update(utensils)

#dinnerdinner=utensils.difference(food)
#dinna=utensils.union(food)
#print(dinna)
#print(dinner_table)
#print(dinnerdinner)



#capitals={'USA': 'Washington',
         # 'india':'Delhi',
        #  'China':'beijing',
        #  'russia':'moscow'}

#print(capitals['China'])
#print(capitals['USA'])
#print(capitals.get("Germany"))
#print(capitals.get("China"))

#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#capitals.update({"germany":"berlin"})
#capitals.update({"USA":"Mumbai"})
#capitals.pop("india")
#capitals.clear()

#for x, value in capitals.items():
  #   print(x, value)



#name="Mr Goteyaa"

#if(name[0].islower()):
 #   print("It is lowercase")
#elif(name[0].isupper()):
 #   print(name.upper())
#else: print(name.count("a"))

#first_name=name[0:2].upper()
#last_name=name[3:].lower()
#names=first_name+" "+last_name
#print(first_name)
#print(last_name)
#print(names)




#def hello():
    #print("Hello World")
    #print("hehehehe")
   # name="oopy goopy"
   # if len(name)>4:
   #     print("greater than 4")
   # else: print("less than 4")
#    print(name+" eeeee")

#def hello(firstname, lastname, age, gender):
 #   print("hola "+name)
  #  print("hoho "+firstname)
   # print("hihi "+lastname)
    #print("you are "+str(age) +" years old")
    #print("you are "+gender)

#hello("bruh")
#hello("huhuhuhuuh")
#name=input("what is your name?")
#hello(name.upper())
#firstname=input("what is your first name? ")
#lastname=input("what is your last name? ")
#name=firstname+" "+lastname
#age=input("what is your age? ")
#gender=input("what is your gender? ")
#ello(firstname, lastname, age, gender)




#def multiply(no1, no2):
 #   result = no1*no2
  #  return result

#print(multiply(2,3))

#def add(no1,no2):
 #   return no1+no2
#print(add(2,3))

#x=add(3,4)
#y=multiply(3,4)
#print(add(x,y)*7)




#def hello(first, second, third):
 #   print("hello "+first+" "+second+" "+third+" Your full name is "+first+" "+second+" "+third)
#hello(first="ranjit", second="raj", third="goenka")




#def multiply(*args):
 #   product = 1
  #  for i in args:
   #     product*=i
    #return product
#print(multiply(1,2,3,4))


#first = input("What is your first name? ")
#second = input("What is your second name? ")
#last = input("What is your last name? ")
#title = input("What is your title? ")
#if len(second)==0:
 #   second=""
#else: second==second
#if title.lower()=="mr" or title.lower()=="mister":
 #   title = "Mr"
#elif title.lower()=="Mrs":
 #   title = "Mrs"
#else: title=""

#def hello(**kwargs):
 #   print("Hello", end=" ")
  #  for key, value in kwargs.items():
   #     if value=="":
    #        print("", end="")
     #   else:
      #   print(value, end=" ")

#hello(title=title,first=first.capitalize(), second=second.capitalize(), last=last.capitalize())




#animal=input("what animal would you like to jump over the moon?")
#animal=animal.lower()
#country=input("what country would you like to go to?")
#country=country.capitalize()
#print("The {} jumped over the moon in the country of {}".format(animal,country))


#name="ranjit"
#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:20} and I am a boy".format(name))
#print("Hello, my name is {:>20} and I am a boy".format(name))
#print("Hello, my name is {:^19} and I am a boy".format(name))


#number=0.123456789
#print("the number is {:.2f}".format(number))
#print("the number is {:.9f}".format(number))
#print("the number is {:.10f}".format(number))
#print("the number is {:.15f}".format(number))


#Number = 123456789
#print("the number is {:b}".format(number))
#print("the number is {:,}".format(number))
#print("the number is {:x}".format(number))
#print("the number is {:E}".format(number))




#import random

#x=random.randint(1,110)
#y=random.random()
#print(x)
#print(y)

#list=["rock", "paper", "scissors"]
#z=random.choice(list)
#print(z)

#cards=[1,2,3,4,5,6,7,8,9,"queen","king","ace","jack"]
#random.shuffle(cards)
#print(cards)


#game=input("Rock, Paper, Scissor, SHOOT ")
#if game.lower()=="rock":
#    print("Paper ", end="HAHA I win again!")
#elif game.lower()=="paper":
 #   print("Scissor ", end="HAHA I win again!")
#elif game.lower()=="scissor":
 #   print("Rock ", end="HAHA I win again!")



#try:
#    num=int(input("Enter numerator "))
 #   den=int(input("enter denominator "))
  #  result = num/den

#except Exception:
    #print("there was an error")
#except ZeroDivisionError as e:
 #   print(e)
  #  print("You cannot divide numbers by 0")
#except ValueError as e:
 #   print(e)
  #  print("enter only numbers")
#else: print(result)
#finally: print("this will always excecute")





#import os
#path = "/Users/ranjitrajgoenka/Desktop/ranjit"
#if os.path.exists(path):
#    print("the path exists")
#if os.path.isfile(path):
#    print("it is a file")
#elif os.path.isdir(path):
#    print("it is a directory")
#else: print("that doesnt exist")

#with open('testing') as file:
   # print(file.read())
#print(file.closed)




#text="hello\nthe \"\\n\" means a new line.\nThis is the 3rd line."
#with open('testing', 'w') as file:
    #file.write(text)

#text = "\nhello im adding the 4th line in the next line of code.\n This is the 5th line.\nIm using the append command."
#with open('test', 'a') as file:
#    file.write(text)
#print("Note that the code will keep adding or appending your text as many times as you run it.")




#import shutil
#shutil.copyfile('testing', 'copy.txt')
#shutil.copy()
#shutil.copy2()




#import os
#source="test"
#destination="/Users/ranjitrajgoenka/Desktop/python/test"

#try:
 #   if os.path.exists(destination):
  #      print("there is already a file here")
   # else:
    #    os.replace(source, destination)
 #       print(source+" was moved")

#except FileNotFoundError:
 #   print(source+" was not found")



#help("modules")



#import random
#while True:
 #choices = ["rock", "paper", "scissors"]
 #computer = random.choice(choices)
 #player = None
 #while player not in choices:
  # player = input("Rock, paper, or scissors?").lower()

 #if player == computer:
  #  print("computer: " + computer)
   # print("player: " + player)
    #print("The game is a tie")

 #elif player=="rock":
  #  print("computer: " + computer)
  #  print("player: " + player)
  #
    # if computer=="scissors":
    #    print("You win!")
    #elif computer=="paper":
     #   print("You lose!")
 #
 #elif player=="paper":
  #  print("computer: " + computer)
   # print("player: " + player)

    #if computer=="rock":
     #   print("You win!")
    #elif computer=="scissors":
     #   print("You lose!")

 #elif player=="scissors":
   # print("computer: " + computer)
    #print("player: " + player)

    #if computer=="paper":
     #   print("You win!")
    #elif computer=="rock":
     #   print("You lose!")

 #playagain=input("Do you want to play again(yes/no)?").lower()
 #if playagain=="yes":
  #  print("Okay, lets go again!")
 #else:
  #break
#print("Bye, have a nice day.")





#def new_game():
 #   guesses=[]
  #  correct_guesses=0
   # question_num=1

    #for key in questions:
     #   print("_____________________")
      #  print("Q. "+str(question_num))
       # print(key)
        #for i in options[question_num-1]:
         #   print(i)
        #guess=input("A, B, C or D?: ").upper()
        #guesses.append(guess)

        #correct_guesses += check_answer(questions.get(key), guess)
        #question_num+=1

#    display_score(correct_guesses, guesses)

#if answer == guess:
  #   print("You're correct!")
   #  return 1
# else:
 #    print("You're wrong!")
  #   return 0

#def display_score(correct_guesses, guesses):
 # print("_____________________")
  #print("RESULTS")
  #print("_____________________")

  #print("Answers: ", end = " ")
  #for i in questions:
   #   print(questions.get(i),end=" ")
  #print()

  #print("Guesses: ", end=" ")
  #for i in guesses:
   #   print(i, end=" ")
  #print()
  #print()
  #score=correct_guesses/len(questions)*100
  #print("Your score is "+str(score))



#def play_again():
# response=input("Do you want to play again(yes/no)?").lower()
 #if response=="yes":
  #   return True
 #else: return False

#questions = {"1+1=?: ": "A",
 #            "2+2=?: ": "A",
  #           "3+3=?: ": "D",
   #          "4+4=?: ": "B",
    #         "5+5=?: ": "C"
     #        }

#options = [["A. 2", "B. 2.1", "C. 2.2", "D. 2.3"],
 #          ["A. 4", "B. 4.1", "C. 4.2", "D. 4.3"],
  #       ["A. 8.2", "B. 8", "C. 8.1", "D. 8.3"],
    #       ["A. 10.2", "B. 10.1", "C. 10", "D. 10.3"]]


#new_game()
#while play_again():
 #   new_game()
#print("OKAY bye!")





# class Car:
#
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def drive(self):
#         print("This "+str(self.year)+" "+self.color+" "+self.model+" is driving.")
#
#     def stop(self):
#         print("This "+str(self.year)+" "+self.color+" "+self.model+" is stopped.")
#
#
# car_1 = Car("Chevy", "Corvette", 2021, "Blue")
# car_2 = Car("Ford", "Mustang", 2023, "Red")
# print(car_1.make)
# print(car_1.color)
# print(car_1.model)
#
# car_1.drive()
# car_1.stop()
#
# car_2.drive()




# class Animal:
#
#     alive=True
#
#     def eat(self):
#         print("This animal is eating.")
#
#     def sleep(self):
#         print("This animal is sleeping.")
#
#
# class Rabbit(Animal):
#     def run(self):
#         prin("This animal is running.")
#
# class Fish(Animal):
#     def swim(self):
#         print("This animal is swiming.")
#
# class Hawk(Animal):
#     def fly(self):
#         print("This animal is flying.")
#
# rabbit=Rabbit()
# fish=Fish()
# hawk=Hawk()
#
# print(rabbit.alive)
# fish.fly()
# hawk.fly()





# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print("This animal is eating.")
#
# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking.")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# Dog.eat(dog)
# dog.bark()





# class Prey():
#     def Flee(self):
#         print("This animal is fleeing.")
#
# class Predator():
#     def Hunt(self):
#         print("This animal is hunting.")
#
# class Rabbit(Prey):
#     def Jump(self):
#         print("This animal is jumping.")
#
# class Lion(Predator):
#     def Roar(self):
#         print("This animal is roaring.")
#
# class Fish(Prey, Predator):
#     def swim(self):
#         print("This animal is swimming.")
#
#
# rabbit = Rabbit()
# lion = Lion()
# fish = Fish()
#
# rabbit.Jump()
# lion.Roar()
# rabbit.Flee()
# fish.Flee()
# fish.Hunt()




print("Hello World")
jnvdaebnioeubtaeutboetbnetnbotb




























