#add service charge to each purchase

TICKET_PRICE = 10

tickets_remaining = 100

#ask for name

name = input ("What is your name? ")
print("Thank you, {}.".format(name))
  #raise NameError("Please type your name")

#ask how many tickets they would like and output how many tickets are remaining using tickets_remaining

while tickets_remaining >= 1:
  purchase_number = input ("How many tickets would you like? There are {} remaining. ".format(tickets_remaining))
  try:
    purchase_number = int(purchase_number)
    if purchase_number > tickets_remaining:
      raise ValueError("There are not that many tickets available.")
  except ValueError as err:
    print("It seems we've run into an issue. Please try again.".format(err))
  else:

#output total to screen

    total_cost = TICKET_PRICE  * purchase_number
    print("That will be ${}.".format(total_cost))
    print("Would you like to buy " + str(purchase_number) + " tickets?")
    confirm = (input("(Y/N) "))

  #prompt user to confirm order

    if confirm.lower() == ("y" or "yes"):
      print("Thank you! Your purchase is complete!")
      tickets_remaining -= purchase_number

    else:
      print("Please start your order over to make corrections.")

print("Tickets are sold out, sorry.")
