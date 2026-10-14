nyc_girl = 0
paris_girl = 0
la_girl = 0
london_girl = 0

answer1 = input("What is your favorite season? A fall, B winter, C spring, D summer?")
if answer1 == "A" or "a":
    london_girl += 1
elif answer1 == "B" or "b":
    nyc_girl += 1
elif answer1 == "C" or "c":
    paris_girl += 1
elif answer1 == "D" or "d":
    la_girl += 1

answer2 = input("What is your favorite breakfast food? A bagel, B croissant, C avacado toast, D eggs and toast?")
if answer2 == "A" or "a":
    nyc_girl += 1
elif answer2 == "B" or "b":
    paris_girl += 1
elif answer2 == "C" or "c":
    la_girl += 1
elif answer2 == "D" or "d":
    london_girl += 1

answer3 = input("What is your favorite drink? A smoothie, B tea, C matcha, D espresso")
if answer3 == "A" or "a":
    la_girl += 1
elif answer3 == "B" or "b":
    london_girl += 1
elif answer3 == "C" or "c":
    nyc_girl += 1
elif answer3 == "D" or "d":
    paris_girl += 1

answer4 = input("What kind of jacket do you like? A puffer, B workout jacket, C trench coat, D pea coat")
if answer4 == "A" or "a":
    nyc_girl += 1
elif answer4 == "B" or "b":
    la_girl += 1
elif answer4 == "C" or "c":
    paris_girl += 1
elif answer4 == "D" or "d":
    london_girl += 1

answer5 = input("What workout do you like? A bike, B walk, C pilates, D running")
if answer5 == "A" or "a":
    paris_girl += 1
elif answer5 == "B" or "b":
    london_girl += 1
elif answer5 == "C" or "c":
    la_girl += 1
elif answer5 == "D" or "d":
    nyc_girl += 1
print (f"Your score is:NYC {nyc_girl},Paris {paris_girl},LA {la_girl} , and London {london_girl}!")

#you get this ending if your points mostly went to NYC and you are and NYC girl
if nyc_girl > paris_girl and nyc_girl > la_girl and nyc_girl > london_girl:
    print ("You are a NYC girl!")
#you get this ending if your points mostly went to Paris and you are and Paris girl
elif paris_girl > nyc_girl and paris_girl > la_girl and paris_girl > london_girl:
    print("You are a Paris girl!")
#you get this ending if your points mostly went to LA and you are and LA girl
elif la_girl > nyc_girl and la_girl > paris_girl and la_girl > london_girl:
    print("You are a LA girl!")
#you get this ending if your points mostly went to London and you are and London girl
elif london_girl > nyc_girl and london_girl > paris_girl and london_girl > la_girl:
    print("You are a London girl!")