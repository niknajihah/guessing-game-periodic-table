
import random    
def main():
    """Print "WELCOME TO GUESSING GAME ^-^" and return None."""
print("WELCOME TO GUESSING GAME ^-^") 
myName=(input("Hello! What is your name? : "))
print("Good luck",myName,"! Let's start now")


table = ("Aluminum","Barium","Chromium","Platinum","Titanium")
secret = random.choice(table)

print("Clue : Al-13,Ba-56,Cr-24,Pt-78,Ti-22")
guess = True

while guess:
    element = str(input("Enter your guess chemical element based on one of those clues given :"))
    if secret == element:
        print("That element is : ",secret)
        print("Your guess is true!")
        guess = False
    else :
        print("Your guess is false")
else :
        print("Congratulation! Goodbye",myName, "^^")
        
main()