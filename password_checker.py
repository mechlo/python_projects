import sys

MASTER = 'opensesame'
password = input("Please enter a password. ")
attempts = 1
while password != MASTER:
  if attempts > 3:
    sys.exit("Too many attempts.")
  password = input("Incorrect, try again. ")
  attempts +=1
print("Correct.")
