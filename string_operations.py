#1. Write a function to check if a string is a palindrome.
# def check_palindrome(str):
#     reversed_str=str[::-1]
#     if str==reversed_str:
#         print(f'{str} is palindrome')
#     else:
#         print(f'{str} is not palindrome')

# check_palindrome('madam')
# check_palindrome('Gunay')





#2. Create a function to check if two strings are anagrams.

# My first try
# def check_anagrams(str1,str2):
#     for item in str1:
#         a=str2.find(item)
#         if a>0:
#             print('f{str1} and {str2} are anagrams')

# check_anagrams('unay', 'unya') 

# Other options:

# Sorted
# def check_anagrams(str1, str2):
#     if sorted(str1.lower()) == sorted(str2.lower()):
#         print(f'{str1} and {str2} are anagrams')
#     else:
#         print(f'{str1} and {str2} are not anagrams')
# check_anagrams('salam', 'lamas')


# Manual frequency count
# def check_anagrams(str1, str2):
#     def count_chars(s):
#         counts = {}
#         for char in s.lower():
#             counts[char] = counts.get(char, 0) + 1
#         return counts
    
#     if count_chars(str1) == count_chars(str2):
#         print(f'{str1} and {str2} are anagrams')
#     else:
#         print(f'{str1} and {str2} are not anagrams')
# check_anagrams('salam','lamas')

# recursion (the best for me)
# def check_anagrams(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     if not str1:
#         return True
#     char = str1[0].lower()
#     str1 = str1[1:]
#     if char.lower() in str2.lower():
#         str2 = str2.lower().replace(char, '', 1)
#         return check_anagrams(str1, str2)
#     return False

# result = check_anagrams('Listen', 'Silent')
# print('Anagrams' if result else 'Not Anagrams')

#3. Take a string input and print it in reverse order.

# Slicing method:
# def reversing_str(str):
#     reversed_str=str[::-1]
#     print(reversed_str)
# reversing_str('Hello')

# Using for loop:

# def reversing_str(str):
#     reversed_str=''
#     for item in str:
#         reversed_str= item + reversed_str
#     print(reversed_str)
# reversing_str('Hello')

# Using reversded method:
# def reversing_str(str):
#     reversed_str=''.join(reversed(str))
#     print(reversed_str)
# reversing_str('Hello')



# Using recursion:
# def reversing_str(str):
#     if len(str)==0:
#         return str
#     return str[-1]+reversing_str(str[:-1])
# print(reversing_str('hello'))



#4. Write a function that takes a sentence and capitalizes the first letter of each word.

# def capitalizing_words(sentence):
#     splitted_str_list = sentence.split()
#     capitalized_sentence = ""
#     for item in splitted_str_list:
#         capitalized_sentence += item.capitalize() + " "
#     return capitalized_sentence.strip()
# print(capitalizing_words('hello world it is Gunay'))

#5. Create a function to count how many times a substring occurs in a given string.

# def find_substr(main_str,sub_str):
#     num_sub_str=0
#     start=0
#     while True:
#         start=main_str.find(sub_str,start)
#         if start==-1:
#             break
#         num_sub_str+=1
#         start+=1
#     return num_sub_str
# print(find_substr('hello world hello', 'hello'))

# using split mehtod:
def find_substr(main_str,sub_str):
    a=len(main_str.split(sub_str))-1
    return a
print(find_substr('hello world hello', 'hello'))

