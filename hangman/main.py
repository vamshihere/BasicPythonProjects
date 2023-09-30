import random
from words import words_list
# this code only works if the letters in the word are uniue
#todo later write the code for words that have repeated characters too
def hangman():
    target_word = random.choice(words_list).upper()
    print(target_word)
    target_set = set(target_word.upper())
    waste_set = set()
    ans_set = set()
    print(target_set)
    while(len(ans_set) != len(target_set)):
        ch = input("guess a character :").upper()
        if(ch in target_set):
            ans_set.add(ch)
        else:
            waste_set.add(ch)
        print(ans_set)    
        print("your string is ")
        view = []
        for ch1 in target_word:
            if ch1 in ans_set:
                view.append(ch1)
            else:
                view.append('_')
        display = " ".join(view)
        print(display)
        print("and you have used the characters :")
        print(" ".join(waste_set))
    print("hurray you have won!!")
hangman()




    




