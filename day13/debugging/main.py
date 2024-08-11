############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
#     elif i == 13:
#         print(f"You got {i}")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_num)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? 1994  "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.") 

# # Fix the Errors
# age = int(input("How old are you?\n "))
# if age > 18:
#   print(f"You can drive at age {age}.")
# else:
#   print(f'Your ara not eligiable at age of {age}')

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(f"total words are {total_words}")

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])