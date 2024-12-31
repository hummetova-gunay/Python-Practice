# algorithms using recursion:
# 1. Factorial:
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
# print(factorial(5))

# 2. Fibonacci sequence:
def fibonacci_sequence(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        seq=fibonacci_sequence(n-1)
        seq.append(seq[-1]+seq[-2])
        return seq
    
# print(fibonacci_sequence(6))


# 3. Tower of Hanoi:



# 4. Sum of the items in array:
def sum(arr):
    if not arr:
        return 0
    return arr[0]+sum(arr[1:])
print(sum([1,2,3,4,5,6]))

# 5. Reversing a string:
def reverse_str(str):
    if len(str)==0:
        return str
    return str[-1]+reverse_str(str[:-1])
print(reverse_str("hello"))

