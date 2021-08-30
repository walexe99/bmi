vikt = float(input("Skriv vikten du har"))
längd = float(input("Skriv längden du har"))

bmi = vikt / (längd / 100)**2 
print("Din vikt är:", bmi) 

if (bmi > 0):
    if (bmi <= 16):
            print("Du är mycket underviktig") 
                 
    elif(bmi <=18.5):
        print("Du är underviktig")
    elif(bmi <= 25):
        print("Du är frisk")
    elif(bmi <= 30):
        print("Du är överviktig")
    elif(bmi >=30):
        print("Du är mycket överviktig")




