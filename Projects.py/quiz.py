# the purpose of this code is to quiz the user on chemistry


print("Welcome, player")
answer = input("Are you ready to take your test? Y/N: ") # asks the user if they intend to play
if answer.upper() == "Y":
    print("great! let's continue.") # contunues if user picks yes(Y)
else:
    quit()
score = 0 # keeps track of the score
option = """        
a. S 
b. Se
c. Na
d. N"""  # question options
print("Question 1")
print("what is the symbol for selenium? " + option)
choice = input()
if choice.lower() == "b":
    print("That is correct!")
    score += 1
else:
    print("That's not quite right")
print("Question 2")
choice = input("How many neutrons are in sodium? (do not round and type your answer in whole numbers): ")
if choice.lower() == "11":
    print("That is correct!")
    score += 1
else:
    print("That's not quite right")
print("you got " + str(score) + " correct")
solution= input("Would you like to see the solutions? ")
if solution.upper() == "Y":
    print("Question 1. b")
    print("Question 2. 11")
else:
    quit()
input("Thank your for playing.")









