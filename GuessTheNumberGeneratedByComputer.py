import random
low = int(input("give me the lower bound "))
high = int(input("give me the upper bound "))
random_number = random.randint(low,high)
x = int(input(f"guess the number between {low} and {high} "))
while(True):
    if(x < random_number):
        x = int(input(f"{x} is lower please guess a higher number than this "))
    elif(x > random_number):
        x = int(input(f"{x} is higher please guess a lower number than this "))  
    else:
        print(f" Hurray!! you have guessed it corrrectly")
        break


