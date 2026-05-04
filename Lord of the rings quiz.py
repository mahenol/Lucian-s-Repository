'''This program quizes the user about the 
famous movie franchise lord of the rings'''
correct = 0
highscore = 8
wrong= 0
#This part asks the first question
first = input("How many members are in the Fellowship of the Ring? A/B/C \
  A.Nine   B.Eleven   C.Seven " )
#This part shows if the inputed answer was correct
first = first.upper()
if first == "A":
   correct += 1
else:
   wrong +=  1
print(F"You got {correct}/{highscore}")
