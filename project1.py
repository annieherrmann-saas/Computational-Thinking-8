sign_off_message = "Thanks for interacting with this chatbot have a great day!"
name = input("What is your name?")
print(f"Hello {name} and welcome to this chatbot!")
input()
answer2 = input("What is your favorite animal?") 
if answer2 == "snow leopard":
    print("Wow, snow leopards are my favorite too!")
else:
    print("Those are so cool!")
input()
color = input("What is your favorite color?")
print(f"{color} is my favorite color to!")
input()
answer4 = input("Would you like to continue using this chatbot? yes or no")
if answer4 == "yes":
    print("Ok!")
else:
    quit()
input()
favoriteclass = input("What is your favorite core class?")
if favoriteclass == "science":
    print("Mine to!")
else: 
    print("Oh thats fun mine is science!")
input()
weather = input("What is your favorite type of weather?")
print(f"I love {weather} to!")
input()
movie = input("What is your favorite movie?")
if movie == "ironman":
    print ("Mine too!")
else:
    print ("Oh thats a good movie my favorite is Ironman!")
input()
place = input("Where is your favorite place you've visited?")
print(f"{place} is so cool! I can't choose a favorite place!")
input()
print(sign_off_message)