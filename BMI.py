def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi <29.9:
        return "over weight"
    else:
        return "obese"
 
    
 #Input from user
    
try:
     weight = float(input("Enter your weight in kilograms: "))
     height = float(input("Enter your height in metres: ")) 

     bmi = calculate_bmi(weight, height)         
     category = get_bmi_category(bmi)   

    
     print(f"\nYour BMI is: {bmi:.2f}")      
     print(f"You are classified as: {category}")  
except ValueError:
                 print("Please enter valid numbers for weight and height.")         