import random
target = random.randint(1,100)
print("target will be between 1 to 99")
i = 0
flag = 0
while i<3:
    guess = int(input("enter number"))
    if(guess < target):
        print("guess is lesser")
    elif(guess > target):
        print("guess is larger")
    else:
        print("won")
        flag = 1
        break
    i = i+1
    
if flag == 0:
    print("lost number is ",target)
# output:
# target will be between 1 to 99
# enter number 25
# guess is lesser
# enter number 29
# guess is lesser
# enter number 58
# guess is larger
# lost number is  36
