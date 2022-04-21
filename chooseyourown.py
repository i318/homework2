


from tkinter import N


name = input("Enter your username: ")
if name.isalpha() == False:
    print("Use alphabetical letters only. ")



print("Welcome,", name,". From here on, you shall embark on your journey to reveal your final fate! Based on the book All Tomorrow's. " )

answer = input("Humanity is doomed. The Qu have survived every atomic bomb sent by the humans. You are in charge of making the final call.\
    Do you want to unleash a highly developed plague (1) to weaken the Qu, or use mecha suits?(2) Choose 1 or 2:  ")  
#ask user for answer to question above
if answer == "1":
    a2= input("It was highly ineffetive. The Qu do not have weak immune systems like humans. They bioengineered their DNA to be flawless. Now, you lost the hopes of people who believed you could save the world. You walk down the street after this failure and see a glowing powder on the ground.\
        Do you want to pick it up (1) or not (2):  ")
    if a2 == "1":   
        a5 = input("This powder was a remnant of the Qu's attack on the humans. You have made an amazing discovery. Do you want to hand it to the government[1] or use it yourself?[2]")
        if a5 == "1": #users answer to hand it to the government
            print("The government deemed the powder worthless and suspiciously disappeared. They used the powder to become Qus and left humanity. Ggs")
        elif a5 == "2":
            print("Touching the powder turned you into a Qu. Now you can decide if you want to side with humanity or not[on your own].")
        else:
            print("Not a valid option. You lose")
    elif a2 == "2":  #did not pick up powder
        print("You ignored the powder. It was probably worthless. Now you carry on home and drink so much that you pass out. You lost.")
    else:
        print("Not a valid option. You lose")
   #Answer the question 1      
elif answer == "2": 
    a3 = input("The mecha suits you engineered were strangely effective. The Qu population decreased by 10% thanks to your expertise. Now, do you want to celebrate(1) or not (2): ")
    if a3 == "1": #celebrated the success
        print("Celebrating was a bad idea, because the Qu invaded. Sorry, you died")
    elif a3 == "2": #did not celebrate 
        a4 = input("Not celebrating was wise, the Qu invaded while everyone was gone. Do you want to unleash humanity's final defense by clicking a button? Yes = 1, No = 2: ")
        if a4 == "1":  
            print("You suceeded. Humanity lives on a bit longer. ")
        elif a4 == "2": 
            print("You should've used it. Now, we all explode.")
        else:
            print("Not a valid option. You lose")

else: 
    print("You died. Sorry. ")

print("Thank you,", name, "for playing. ")