print("Welcome to my countries quiz")


playing = input("Do you want to gain proficiency in geography? Yes or No:  ").lower

if playing == "no":
    quit()

print("Now--we shall start the game.")

 


def questions():
    score = 0
    answer = input("What is the capital of Canada? ")
    if answer == "Ottowa":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%") 
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%") 

    answer = input("What is the capital of Russia? ")
    if answer == "Moscow":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of U.S.A? ")
    if answer == "Washington":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")       
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of Fiji? ")
    if answer == "Suva":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")        
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")

    answer = input("What is the capital of Nepal? ")
    if answer == "Kathmandu":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")        
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")        
    answer = input("What is the capital of Sweden? ")
    if answer == "Stockholm":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")        
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of U.K? ")
    if answer == "London":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of India? ")
    if answer == "New Delhi":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of China? ")
    if answer == "Beijing":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")
    else:
        print("Incorrect. ")
        print(score) 
        print(str((score/ 10) * 100) + "%")
    answer = input("What is the capital of Ghana? ")
    if answer == "Accra":
        print("Correct")
        score = score + 1
        print(score)
        print(str((score/ 10) * 100) + "%")
    else:
        print("Incorrect. ")
        print(score)
        print(str((score/ 10) * 100) + "%") 

questions()

playagain = input("Would you like to play again? Yes or No?  ").lower

if playagain == "no":
    quit()














