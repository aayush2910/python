
#calculator for 2 no.

# print('calculator')

# opr=input('choose your operator [*,/,+,-]\n')

# a=float(input("Enter the first no."))
# b=float(input("enter the other no."))



# if opr == '+':
#     print(a+b)
# elif opr =='*':
#     print(a*b)
# elif opr=='/':
#     print(a/b)
# elif opr =='-':
#     print(a-b)
#     exit()
# else:
#     print("wrong input")
    
#   {{{{{
# from random import shuffle


# def shuffle_list(my_list):
#     shuffle(my_list)
#     return my_list

# hi_list = ['o','','']

# shuffle_list(hi_list)
# result = shuffle_list(hi_list)
# print(result)

# def player_guess(guess):
#     if guess not in ['0','1','2']:
#         print("INVALID ! pick the no.:'0','1','2'")
#         return int(guess)
    
# guess=input("Enter the guess:")

# player_guess=player_guess(guess)

# print(player_guess)

# count=0
# if guess and shuffle_list == 0:
#     print("you won")
#     count+=1

#        }}}}} 


#print table of any no. using for and while loop

# a= int(input("Enter the no the table you want:"))

# for i in range (1,11):
#     b=a*i
#     print(f"5*{i}={b}")
# i=1
# while i<11:
#     b=a*i
#     print(f"5*{i}={b}")
#     i+=1

#this code is to print sum of first n no. using while loop.
# n= int(input("Enter the no till you want the sum:"))
# i=1
# sum=0
# while i<=n:
#     sum += i
#     print(sum)
#     i+=1

# def fac_recurse(n):
#     if n==1 or n==0:
#         return 1; #base case
#     return n*fac_recurse(n-1)

# #recursive call
# f=fac_recurse(5)
# print(f)

# This is the program for sum of n natural no. using function
# def sum_first_N(n):
#     if n==0:
#         return 0
#     return n+sum_first_N(n-1)


# S=sum_first_N(0)
# print(S)


#this is the code for converting celcius into farhnite(spelling may be wrong!\)
# def cel_to_far(value):
#     f= ((9/5)*value)+32
#     return f

# far=cel_to_far(0)
# print(far)



#     """This Function prints stars"""
# def print_stars(n):

#     i=0
#     while i<=n:
#         print('*'*(n-i))
#         i+=1


# print_stars(3)        


#THIS IS THE ROCK, PAPER AND SCIESOR GAME

from random import randint

print("Opponent's turn: Rock(R) , Paper(P) and Sciesor(S) :  \n")
rand_no= randint(1,3)
if rand_no == 1:
    Opponent ='R'
elif rand_no==2:
    Opponent='S'
else :
    Opponent = 'P'

you=input("Your turn :\nRock(R) \nPaper(P) \nSciesor(S) : \n ")

def win_or_lose(player_1,your_guess):
    if player_1 == your_guess:
        print('Match is tie!')
    elif (player_1=='R'):
        if your_guess == 'S':
            print ('You lose! ')
        elif your_guess == 'P':
            print ("Congratulations You won!")
    elif player_1 == 'P':
        if your_guess == 'R':
            print ('You lose! ')
        elif your_guess == 'S':
            print ("Congratulations You won!")
    elif player_1 == 'S':#scissor case
        if your_guess == 'P':
            print ('You lose! ')
        elif your_guess == 'R':
            print ("Congratulations You won!")

print(f"\nOpponent choose :{Opponent} ")
print(f"you choose :{you}\n")

win_or_lose(Opponent,you)







