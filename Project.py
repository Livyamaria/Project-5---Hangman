import random
from asciiart import stages
from logo import logo_name
print(logo_name)
word_list = ["aardvark", "baboon", "camel","wave","joyful","youthful"]
word = random.choice(word_list)

#_______________________________________randomly selected word__________
stage=len(stages)-1
game=False
#---------------------------------------found the length of the asciiart---------------------------------------------
list_word =[]
for letters in word:
    list_word.append(letters)
#-----------------------------------------selected word stored in the list named list_word--------------------------------------------
length=len(list_word)

display = []
for _ in range(length):
    display += "_"
#-------------------------------------------for displaying dashes in the screen with the length of the word--------------------------------------------
while not game:
  user = input("Hey user you can enter the letter comes in your mind : ").lower()

  if user in display:

    print(f"You have already guessed{user}" )
  if user in list_word:
   for position in range(length):
       match = list_word[position]
       if match==user:
           display[position]=match
  print(f"{' '.join(display)}")
#-------------------------------------- if word is present  place in the display instead of dashes-------------------
  if user not in list_word:
    print(f"You guessed {user},that's not in the word.You lose a life")
    stage-=1
    if stage==0:
        game=True
        print("you lose")
  if not "_" in display:
        game=True
        print("you win")
  print(stages[stage])





