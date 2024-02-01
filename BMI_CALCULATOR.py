height = float(input("Enter the height in inches: "))
weight = float(input("Enter weight in lbs: "))

def BMI(height, weight):
    bmi = weight/(height**2) * 703

    if(bmi<18.5):
        return 'underweight', bmi

    elif(bmi>=18.5 and bmi<25):
        return 'Healthy', bmi

    else:
        return 'overweight', bmi


quote, bmi = BMI(height,weight)
print("Your bmi is {} and you are {}". format(bmi, quote))