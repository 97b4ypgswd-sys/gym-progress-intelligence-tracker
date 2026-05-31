print("===================================")
print(" GYM PROGRESS INTELLIGENCE TRACKER ")
print("===================================")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))
goal = input("Goal (fat loss / muscle gain / maintenance): ").lower()

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print("\n----------- REPORT -----------")
print("Name:", name)
print("Age:", age)
print("Weight:", weight, "kg")
print("Height:", height_cm, "cm")
print("BMI:", round(bmi, 2))

# BMI Analysis
if bmi < 18.5:
   bmi_status = "Underweight"
elif bmi < 25:
   bmi_status = "Normal Weight"
elif bmi < 30:
   bmi_status = "Overweight"
else:
   bmi_status = "Obese"

print("BMI Status:", bmi_status)

# Goal Suggestions
print("\n----------- INTELLIGENCE REPORT -----------")

if goal == "fat loss":
   target_calories = weight * 24 - 400
   protein = weight * 2.2

   print("Recommended Goal: Fat Loss")
   print("Suggested Calories:", round(target_calories))
   print("Suggested Protein:", round(protein), "g/day")
   print("Focus on:")
   print("- Daily steps: 8000-12000")
   print("- Strength training 4-6 days/week")
   print("- High protein diet")

elif goal == "muscle gain":
   target_calories = weight * 24 + 300
   protein = weight * 2.0

   print("Recommended Goal: Muscle Gain")
   print("Suggested Calories:", round(target_calories))
   print("Suggested Protein:", round(protein), "g/day")
   print("Focus on:")
   print("- Progressive overload")
   print("- Sleep 7-9 hours")
   print("- Calorie surplus")

elif goal == "maintenance":
   target_calories = weight * 24
   protein = weight * 1.8

   print("Recommended Goal: Maintenance")
   print("Suggested Calories:", round(target_calories))
   print("Suggested Protein:", round(protein), "g/day")

else:
   print("Unknown goal entered.")

# Strength Score
strength_score = (weight * 0.6) + (age * 0.4)

print("\nEstimated Fitness Score:", round(strength_score, 1))

if strength_score < 40:
   print("Level: Beginner")
elif strength_score < 70:
   print("Level: Intermediate")
else:
   print("Level: Advanced")

print("\nThank you for using Gym Progress Intelligence Tracker!")