import random
from game_data import data
from art import logo,vs


def getData(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}"


def checkAnswer(guess,a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {getData(account_a)}")
  print(vs)
  print(f"Against B: {getData(account_b)}")

  # Ask User for a guess

  guess = input("Who has more followers? Type 'A' OR 'B'").lower()

  # check if user is correct
  # get followers count of each account

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  is_correct = checkAnswer(guess,a_follower_count,b_follower_count)

  if is_correct:
    score += 1
    print(f'You are right your score  {score}')
  else:
    game_should_continue = False
    print(f'Sorry, You are wrong your score {score}')

