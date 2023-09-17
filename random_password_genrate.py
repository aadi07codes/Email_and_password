#--------------------Randomly Password Genrated--------------------------------------------------------------------------#
import random
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*_"  # character which is randomly choice
a = 1
b = 6
n = random.randint(a,b)                           #  How many password do you want randomly select
print('Your Password Succesfully Genrated :',n)
for i in range (0,n):                             #  how many password do you want?
    for i in range (0,8):                         #  password character length
        if len(character)>=8:                     #  condition character length eqqual and not less than 8
            ps = random.choice(character)         #  random.choice() for randomly selection of charaacter
            print(ps,end='')
        else:
            print("Password length should be minimum : 8")
    print("\n",end='')