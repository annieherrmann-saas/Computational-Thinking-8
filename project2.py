sign_off_message = "Bye!"
place1 = input("You wake up, what do you want to do today? Choose from starbucks, the mall, chipotle, and ice cream")
if place1 == "Starbucks":
    starbucks1 = input("Do you want an iced chai or a pumpkin spice latte?")
    if starbucks1 == "iced chai":
        print("you got a chai. yum!")
    elif starbucks1 == "pumpkin spice latte":
        print("you got a pumpkin spice latte. yum!")
    else:
        print("delicious!")

elif place1 == "mall":
    mall1 = input("Do you want to go to hollister, brandy, garage, or aritzia??")
    if mall1 == "hollister":
        print("you got the cutest top and bikini!")
    if mall1 == "brandy":
        print("you got a really cute matching set!")
    if mall1 == "garage":
        print("you got a tanktop")
    if mall1 == "aritzia":
        print("you got a hoodie,and matching sweatpants")
    else:
        print("you left the mall with nothing")

elif place1 == "chipotle":
        chipotle1 = input("do you want a burrito or a bowl?")
        if chipotle1 == "bowl":
            print("great you got a delicious bowl!")
        if chipotle1 == "burrito":
            print("wrong choice your getting a bowl!")
        else:
         print("you got a bowl")
     
elif place1 == "ice cream":
    icecream1 = input("do you want mint oreo or vannila!")
    if icecream1 == "mint oreo":
        print("great choice that is the best flavor you got it in waffle cone!")
    if icecream1 == "vanilla":
        print("great! you got it in a waffle cone!")
    else:
        print("welp you didn't get ice cream")
else:
    print("welp you sat in your bed all day")

print(sign_off_message)