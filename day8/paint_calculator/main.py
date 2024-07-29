import math

def paint_calc(height,width,cover):
  num_cans = (height * width)/cover
  round_up_can = math.ceil(num_cans)
  print(f"You need {round_up_can} cans to paint wall")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("enter height of wall: ")) # Height of wall (m)
test_w = int(input("enter width of the wall: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
