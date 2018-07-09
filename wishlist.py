
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinny",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]


books.insert(0,"Learning Python: POOP")
books[0] += " - Mark Lutz"

print ("Suggested gift: {}".format(books[0]))

print("Books:")
for book in books:
  print("* " + book)

def wishlist(name,wishes):
  items = wishes.copy()
  print(name + ": ")
  suggested_gift = items.pop(0)
  print(">>>", suggested_gift, "<<<")
  for item in items:
    print("* " + item)
  print()

wishlist("Books",books)
wishlist("Games",video_games)
