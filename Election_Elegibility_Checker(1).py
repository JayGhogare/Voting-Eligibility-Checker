Age = int(input("Enter your Age:"))



if Age >= 18:
   Card = input("Do you have your Voting Card? (Yes/No):").lower()
   if Card == "yes":
        print("You are eligible to Vote, Thankyou!!")
   elif Card == "no":
        print("Please make your Voting Card first") 
else :
    print("You are not eligible to Vote, Sorry!!")           