# print("hello")
# print('hellp')
# first =int(input("enter the first no."))
# b = float(input("Second no."))
# print("the sum of first and b is ",(first + b), "and the first no. is ",(first))
# a=5
# b=34
# print("their sum is ",a+b)
# if a>10:
#     print("a is grater")
# else:
#     print("a is less than 10")
# my_str="abcdefghijkl"
# print(my_str)
# #[start:stop:step]----the start will include the no. whereas the stop will not include and the step is for jumping of the given no.
# print(my_str[0:6:2])
# a="tinker" 
# print(a)
# print(a[-5:-2])
#here we go for formating of string
#two methods are there the @first one is -->( .format method )
# print('this is a string {}'.format('formating'))
# print('In there family there lived {2},{1} and one their {0}'.format('son', 'mother','father'))
# print(11>6) this is the example of boolean
# print(a['k1']['k2'])

# this is the program for the particular odd or even no between two no...
# a=int(input("Enter the first range:"))
# b=int(input("Enter the last range:"))

# for r in range(a,b):
#     if r%2==0:
#         print(f'even no.:{r}')
#     else:
#         print(r)


from random import randint

random_no = randint

count =0
a=int(input("Enter the lower range: "))
b=int(input("Enter the upper range: "))

print('Random number is:',randint(a,b))

guess = int(input("Guess the no.:"))


def guess_user(guess,count):
    if guess > random_no:
        print("Try Again! You guessed too high.")
    elif guess < random_no:
        print("Try Again! You guessed too low.")
    else:
        print("correct")
        count+=1
        print("count",count)
    return count
     


count = guess_user(guess,count)