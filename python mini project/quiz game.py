from multiprocessing.connection import answer_challenge

print("Welcome to my quiz!")

playing =   input("Do you want to play? ")

if  playing.lower() !=  "yes":
    quit()

print("Okay!:)")
score   =   0;
#q1
answer  =   input("What does CPU stand for? ")
if  answer.lower()  ==  "central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect")
#q2
answer  =   input("What does GPU stand for? ")
if  answer.lower()  ==  "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect")
#q3
answer  =   input("What does RAM stand for? ")
if  answer.lower()  ==  "random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect")

print("you have scored  " +   str(score)   +   "    points")