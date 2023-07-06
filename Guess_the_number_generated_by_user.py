low = int(input("give me the lower bound "))
high = int(input("give me the upper bound "))
while(low <= high):
    mid = (low+high)//2
    response = input(f"is your ans {mid} ? ")
    if(response == 'y'):
        print("I guessed it correctly")
        break
    elif(response =='n'):
        x = input(f"is your number greater than {mid} ? (give a response by y or n)")
        if(x =='y'):
            low = mid+1
        elif(x == 'n'):
            high = mid-1
        else:
            print("In valid response, please give either y or n")
    else:
        print("In valid response, please give either y or n")        




