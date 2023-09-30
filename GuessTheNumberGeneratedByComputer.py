import random
print(f"hello, this is guess game. you need to give me the lower and upper bound and I would guess a number between them. \
Also I will give hints to say the number that I have guessed.")
low = int(input("give me the lower bound: "))
high = int(input("give me the upper bound "))
random_number = random.randint(low,high)
print(f" I have guess my number between the range thaat you have mentioned earlier, Now let's see how quickly you could guess my number :)")
x = int(input(f"guess the number between {low} and {high} "))
while(True):
    if(x < random_number):
        x = int(input(f"{x} is lower, please guess a higher number than this."))
    elif(x > random_number):
        x = int(input(f"{x} is higher, please guess a lower number than this."))  
    else:
        print(f" Hurray!! you have guessed it corrrectly")
        break


