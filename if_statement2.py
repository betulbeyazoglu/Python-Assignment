print ("For the questions below give an answer yes or no")

#if age equals to yes then set con1 to True

age = input("Are you a cigarette addict older than 75 years old :")

if age in ('Yes', 'yes'):

    con1 = True

else:

    con1 = False

#if chronic equals to yes then set con2 to True

chronic = input("Do you have a severe chronic disease :")

if chronic in ('Yes', 'yes'):

    con2 = True

else:

    con2 = False

#if immune equals to yes then set con3 to True

immune = input("Is your immune system too weak :")

if immune in ('Yes', 'yes'):

    con3 = True

else:

    con3 = False

#check if any of the cons are true

coronavirus = con1 or con2 or con3

if coronavirus == True :

    print("You are in risky group")

else:

    print("You are not in risky group")
