#1. Create a function that checks if a given number is odd or even.
# number1=int(input('Please enter a number '))
# def odd_even(num):
#     if num%2==0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
# #odd_even(number1)


#2. Print numbers from 1 to 50. For multiples of 3, print "Fizz"; 
#for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz".

# for num in range(1,51):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%5==0:
#         print("Buzz")
#     elif num%3==0:
#         print("Fizz")
#     else:
#         print(num)

#3. Write a function that calculates the factorial of a given number using a loop.
# fact_num=int(input('please enter a number '))
# factorial=1
# for i in range(1, fact_num+1):
#     factorial=factorial*i
# print(factorial)

#4. Create a function to check if a given number is prime.
# number4=int(input('please enter a number '))
# def is_prime(num):
#     if num>1:
#         for i in range (2,num):
#             if num%i==0:
#                 print(f'{num} is not a prime')
#                 return
#         print(f"{num} is prime")
#     else:
#         print(f'{num} is not a prime')
# is_prime(number4)

#optimized version:
# import math
# def is_prime_optimized(num):
#     if num > 1:
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 print(f"{num} is not a prime")
#                 return
#         print(f"{num} is prime")
#     else:
#         print(f"{num} is not a prime")
# is_prime_optimized(number4)