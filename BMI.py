txt = "BMI Calculator"
x = txt.center(70, '-')
print(x)
print('\n')

height = float(input('Enter your height (in cm):'))
weight = float(input('Enter your weight (in kg):'))

def BMI(height, weight):
    bmi = weight/(height**2)*10000
    if(bmi < 16):
        return 'severly underweight.', bmi
    
    elif (bmi >= 16 and bmi < 18.5):
        return 'Underweight.', bmi
    
    elif (bmi >= 18.5 and bmi < 25):
        return 'healthy.', bmi
    
    elif (bmi >= 25 and bmi < 30):
        return 'overweight.', bmi
    
    elif (bmi > 30):
        return 'obese.', bmi
    
quote, bmi = BMI(height, weight)
print('Your BMI is: {} and you are {}'.format(bmi, quote))