import random
word_list=["HEIGHT","WEIGHT","BOOK","PEN","CLASS","PYTHON"]
word=random.choice(word_list)
length=len(word)
print("length of the word to be guessed is",length)
letter=[]
for _ in range(len(word)):
    l=str(input("enter the letter"))
    letter.append(l)
    print(letter)
word2="".join(letter)
RES=word2.upper()
print("Guessed word is",RES)
print("Random word is",word)
if word.upper()==RES:
    print("congorats you guessed the word right")
else:
    print("Better luck next time")
    

    
