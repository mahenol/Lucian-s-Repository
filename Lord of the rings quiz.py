'''This program quizes the user about the 
famous movie franchise lord of the rings'''
correct = 0
HIGHSCORE = 8
wrong = 0
index = 0
#This is a list of all the questions
questions = ["1.How many members are in the Fellowship of the Ring? A/B/C \
                        A.Nine   B.Eleven   C.Seven ", 
             "2.What is the name of the sword, broken and later reforged \
for Aragorn? A/B/C       A.Excalibur   B.Narsil   C.Chunchunmaru ", 
             "3.What creature did Gollum used to be before the ring corrupted \
him? A/B/C          A.Borkle   B.Smeagol   C.Smaug ", "4.Who gives Frodo the \
possession of the One Ring? A/B/C          A.Gandalf   B.Sauron   C.Bilbo \
Baggins ","5.What is the name of the Balrog that Gandalf fights in the Mines \
of Moria? A/B/C A.Vessholm's Vice   B.Ymir's Flaw   C.Durin's Bane ", "\
6.What is the only place in Middle-earth where the One Ring can be destroyed?""\
 A/B/C A.The fires of Mount Doom   B.Uriel's inferno   C.The  Ignis Caldera ","\
7.Who is the leader of the Ents that helps defeat Saruman? A/B/C  A.Uriel   \
B.Treebeard   C.Smaug ", "8.What is the name of the elvish sword that glows \
when orcs are near? A/B/C  A.Syam   B.Xoris   C.Sting "]
#This is a list of all the answers
answers = ["A", "B", "B","C","C","A","B","C"]
#This code asks questions and colletcs answers
print("This is a quiz about the lord of the rings franchise")
for question in questions:
   answer = input(question)
   answer = answer.upper()
   if answer == answers[index]:
      correct = correct + 1
   else:
      wrong = wrong +  1
   index = index + 1
print(F"You got {correct}/{HIGHSCORE}")
if correct == HIGHSCORE:
   print("Congrats you got all answers correct")
else:
   print(f"You got {wrong} wrong you loser")














