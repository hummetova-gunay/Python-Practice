#1. Create a list of squares for numbers 1 to 10 using list comprehension.

# first_list=[1,2,3,4,5,6,7,8,9,10]
# squares_list=[]
# for i in first_list:
#     squares_list.append(i*i)
# print(squares_list)

#2. Write a program to count the frequency of each word in a given string.
# def count_word_frequency(input_string):
#     # Remove punctuation by replacing it with spaces
#     punctuation = ".,!?()[]{};:'\""
#     for char in punctuation:
#         input_string = input_string.replace(char, ' ')

#     # Convert the string to lowercase and split it into words
#     words = input_string.lower().split()

#     # Create a dictionary to store the word counts
#     word_count = {}

#     # Count the frequency of each word
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     # Display the word counts in the desired format
#     for word, count in word_count.items():
#         print(f"{word}: {count}")

# string = "Gunay, you are the best Gunay"
# count_word_frequency(string)




#3. Sort a list of numbers in ascending and descending order.

random_list=[3,2,14,5,16,7,8,4,9,10]
# sorting a list by using built-in functions

# ascending_order=sorted(random_list)
# print(ascending_order)
# different ways of reversing a list 

# # descending_order=ascending_order[::-1]
# # descending_order=list(reversed(ascending_order))
# # descending_order=sorted(random_list, reverse=True)
# # descending_order=ascending_order.reverse() didn't work???
# print(descending_order)

# sorting a list without using any built-in functions only loops "BUBBLE SORT"
# def bubble_sort(arr):
#     for i in range(len(arr)-1,0,-1):
#         swapped=False
#         for a in range(i):
#             if arr[a]>arr[a+1]:
#                 arr[a], arr[a+1]=arr[a+1], arr[a]
#                 swapped=True
                
#         if not swapped:
#             break
        
#     print(arr)
# random_list_copy=random_list[:]
# bubble_sort(random_list_copy)
# the original list modified that's why the new, copied version of the list created using slicing method [:]



#4. Create a tuple with 5 elements and unpack its values into separate variables.
# my_tuple=(2,4,1,6,10)
# a,b,c,d,e=my_tuple
# print(a,b,c,d,e)




#5. Given a 2D list, write a function to transpose the matrix.

# def transposing_lists(list1,list2):
#     for i in range(len(list1[0])):
#         row=[]
#         for item in list1:
#             row.append(item[i])
#         list2.append(row)
#     return list2

# list1=[[1,2,3],[4,5,6]]
# list2=[]
# print(transposing_lists(list1, list2))