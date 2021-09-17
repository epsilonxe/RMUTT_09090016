def calculate_bmi(w, h):
    body_mass_index = w / (h ** 2)
    return body_mass_index

def bmi_meaning(bmi):
    if bmi < 16:
        result = 'Underweight (Severe thinness)'
    elif bmi >= 16 and bmi < 17:
        result = 'Underweight (Moderate thinness)'
    elif bmi >= 17 and bmi < 18.5:
        result = 'Underweight (Mild thinness)'
    elif bmi >= 18.5 and bmi < 25:
        result = 'Normal range'
    elif bmi >= 25 and bmi < 30:
        result = 'Overweight (Pre-obese)'
    elif bmi >= 30 and bmi < 35:
        result = 'Obese (Class I)'
    elif bmi >= 35 and bmi < 40:
        result = 'Obese (Class II)'
    else:
        result = 'Obese (Class III)'
    return result

if __name__ == '__main__':
    weight = float(input('Enter your weight (kg): '))
    height = float(input('Enter your height (m): '))
    bmi = calculate_bmi(weight, height)
    category = bmi_meaning(bmi)
    print(f'Your BMI = {bmi:.2f} --> {category}')