import random

words=['apple','orange','potato','beautiful']
chosen_word=random.choice(words)
display=[]
for i in range(len(chosen_word)):
    display.append('_')
print(display)
lifes=6
while(lifes>0):
    guessed=input("Enter a letter: ")
    found=False
    if guessed in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guessed.lower():
                display[i]=guessed
    else:
        print("Not matching")
        lifes-=1
        print(f"Lifes remaining = {lifes}")

    print(display)
    if ''.join(display)==chosen_word:
        found=True
        print()
        print(20*"--*")
        print("You Won")
        print()
        print(20*"--*")
        break
    elif lifes==0:
        print()
        print(20*"--*")
        print("You lost! No more lifes remaining!!!!")
        print()
        print(20*"--*")
        break
