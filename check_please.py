import math


def split_check(total, number):
  if number <= 1:
    raise ValueError("More than 1 person is required to split the check.")
  cost_per = total/number
  return math.ceil(cost_per)

try:
  total_due = float(input("What is the total? "))
  people = int(input("How many people? "))
  amount_due = split_check(total_due, people)
except ValueError as err:
  print("That is not a valid value.")
  print("{}".format(err))
else:
  print("Each person owes ${}".format(amount_due))
