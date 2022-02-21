print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("How old are you? "))
#age = int(input("How old are you? ")) -assigns an integer value to age you can remove int from age from is_older to create the same value.. you need to add int to indicate that it's an integer
print("Hello! ", name, ",", "Wow! You are", age, "years old!")

health = 10 #You want to leave this defined so you can change the value of health anytime

'''
-alternative-
is_older = int(age) >= 18
print(is_older) 
'''
if age >= 18: 
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health.")
        print("Let's Play!")

        this_or_that = input("First choice... This or That (this/that)? ").lower()
        if this_or_that == "this":
            ans = input("Nice, you followed the path and reach a beautiful statue holding a large sword with an engraving that says 'Will you take the leap and choose courage?' (I will/Something else) ")
            
            if ans == "I will".lower():
                print("You have gathered courage to move to the next level!")
            elif ans == "Something else".lower():
                print("You've decided to not take the sword and proceeded to walk past the statue. However, you trip on a vine and plummet into a bush of thorns. You lose 2 health.")
                health -= 5

            ans = input("You notice that on your right is a rope ladder... and on your left, a dark cave. Which path will you take (ladder/cave)? ")
            if ans == "ladder".lower():
                print("You try to climb the robe ladder and almost make it to the top, but the rope decides to break and you fall. You lose 5 health.")
                health -= 5

                if health <= 0:
                     print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived!")
            elif ans == "cave".lower():
                print("You followed the path through the dark cave. Suddenly, you realize a plethora of crystals diffusing the darkness. You find someone at the end of the tunnel.")

                if health <= 0:
                     print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived and met the mage against all odds! He will grant you any wish.")
        else:
            print("You went down a deeper hole and lost the game.")

    elif wants_to_play == "no":
        print("See ya!")
elif age >=14:
    print("You can play with supervision.")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Play!")
    elif wants_to_play == "no":
        print("Maybe next time!")
elif age == 0:
    print("That is not a valid input.")
else:
    print("You are not old enough to play..")
