'''print("Welcome user")'''


#
def run():
    print("Press 1 to Continue")
    print("Press 2 to Exit")
a=int(input("Press number to Continue and Exit"))
if a==1:
      pass
elif a==2:
    print("thanks dfor visit")

def book():
    print("press 1 for book1: psychology of money")
    print("press 2 for book2: To Kill a Mockingbird")
    print("press 3 for book3: Brave New World")
    print("press 4 for book1: The Silent Patient")
b=int(input("enter book number to continue"))
if b==1:
      print("psychology of Money:-- Timeless Lessons on Wealth, Greed, and Happiness")
      run()
elif b==2:
      print("To Kill a Mockingbird:-- To Kill a Mockingbird and The Great Gatsby,self-improvement guides such as Atomic Habits and The 7 Habits of Highly Effective People")
      run()
elif b==3:
      print("Brave New World:-- Brave New World is a dystopian novel by Aldous Huxley about a futuristic World State where technology controls reproduction")
      run()
elif b==4:
      print("The Silent Patient:--  The Silent Patient is a psychological thriller about Alicia Berenson, a famous painter who murders her husband and then completely stops speaking")  
book()
