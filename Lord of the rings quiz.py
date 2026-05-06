'''This program quizes the user about the 
famous movie franchise lord of the rings'''
correct = 0
HIGHSCORE = 8
wrong= 0
index = 0
#This is a list of all the questions
questions = ["1.How many members are in the Fellowship of the Ring? A/B/C \
                        A.Nine   B.Eleven   C.Seven ", 
             "2.What is the name of the sword, broken and later reforged \
for Aragorn? A/B/C       A.Excalibur   B.Narsil   C.Chunchunmaru ", 
             "3.What creature did Gollum used to be before the ring corrupted \
him? A/B/C          A.Borkle   B.Smeagol   C.Smaug "]
#This is a list of all the answers
answers = ["A", "B", "B"]
for question in questions:
   answer = input(question)
   answer = answer.upper()
   if answer == answers[index]:
      correct = correct + 1
   else:
      wrong = wrong +  1
   index = index + 1
print(F"You got {correct}/{HIGHSCORE}")
